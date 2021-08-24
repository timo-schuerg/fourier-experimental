# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from scipy import signal
import numpy as np



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

t = np.linspace(0, 8*np.pi, 1000)
s = signal.sawtooth(t, width = 1)


df = pd.DataFrame({
    "x": t,
    "y": s,
    "signal": ["sawtooth" for t in t]
})

df = df.append(
    pd.DataFrame({
        "x": t,
        "y": np.sin(t),
        "signal": ["fourier" for t in t]
    })
)

fig = px.line(df, x='x', y='y', color='signal', title='Sawtooth' )

app.layout = html.Div(children=[
    html.H1(children='Test your Fourier approximation skills!'),

    # html.Div(children='''
    #     Dash: A web application framework for Python.
    # '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)