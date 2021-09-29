#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Example package setup script

File: setup.py

Authors: mkielg11

Date: 15-06-2020

"""

from setuptools import find_packages
from setuptools_dso import DSO, setup


xclib_dso = DSO(
    'xclib',
    sources=['xpackage/deps/xclib/cfile.c', ],
    include_dirs=['xpackage/deps/xclib/include/'],
)


setup(
    name='xpackage',
    version='0.0.2',
    author='mkielg11',
    license='MIT',
    packages=find_packages(),
    setup_requires=["cython", "wheel", "setuptools", "setuptools_dso"],
    python_requires=">=3.6",
    install_requires=[
        'numpy',
    ],
    x_dsos=[xclib_dso],
    zip_safe=False,
)
