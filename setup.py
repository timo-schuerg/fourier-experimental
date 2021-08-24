#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

setup(
    author="timo-schuerg",
    author_email='timo82@gmx.net',
    python_requires='>=3.5',
    description="",
    keywords='fourier',
    name='fourier',
    packages=find_packages(include=['fourier', 'fourier.*']),
)
