#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Example package setup script

File: setup.py

Authors: mkielg11

Date: 15-06-2020

"""
import os

from setuptools import find_packages
from setuptools_dso import DSO, setup

if os.name == 'nt':
    # Windows specific compiler and linker arguments
    # _compiler_args = ['-Wall', '-c', ]
    # _linker_args = ['/DLL', ]
    _compiler_args = []
    _linker_args = []
else:
    # Other compiler and linker arguments (posix)
    # _compiler_args = ['-Wall', '-c', '-fPIC', ]
    # _linker_args = ['-shared', ]
    _compiler_args = []
    _linker_args = []


xclib_dso = DSO(
    'xpackage.clib.cfile',
    sources=['xpackage/deps/xclib/cfile.c', ],
    include_dirs=['xpackage/deps/xclib/include/'],
    extra_compile_args=_compiler_args,
    extra_link_args=_linker_args
)


setup(
    name='xpackage',
    version='0.0.5',
    author='mkielg11',
    license='MIT',
    packages=find_packages(),
    setup_requires=["cython", "wheel", "setuptools", "setuptools_dso"],
    python_requires=">=3.6",
    install_requires=[
        'numpy',
    ],
    x_dsos=[xclib_dso, ],
    zip_safe=False,
)
