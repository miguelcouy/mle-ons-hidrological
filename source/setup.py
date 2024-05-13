# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name = 'mle_ons_hidrological',
    version = '0.0.1',
    packages = find_packages(),
    install_requires = [
        'pandas>=2.2.2'
    ]
)