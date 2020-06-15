#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Example package setup script

File: setup.py

Authors: mkielg11

Date: 15-06-2020

"""

from setuptools import setup, find_packages, Extension
from distutils.command.build_ext import build_ext


class CTypes(Extension):
    pass


class build_ext_rev(build_ext):
    def build_extension(self, ext):
        self._ctypes = isinstance(ext, CTypes)
        return super().build_extension(ext)

    def get_export_symbols(self, ext):
        if self._ctypes:
            return ext.export_symbols
        return super().get_export_symbols(ext)


xclib_extension = CTypes(
    'xclib',
    sources=['xpackage/deps/xclib/cfile.c', ],
    include_dirs=['xpackage/deps/xclib/include/'],
)


setup(
    name='xpackage',
    version='0.0.1',
    author='mkielg11',
    license='MIT',
    packages=find_packages(),
    setup_requires=["cython", ],
    python_requires=">=3.6",
    install_requires=[
        'numpy',
    ],
    ext_modules=[
        xclib_extension
    ],
    cmdclass={'build_ext': build_ext_rev},
)
