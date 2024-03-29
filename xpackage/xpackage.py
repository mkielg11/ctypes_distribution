#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Example package file

File: xpackage.py

Authors: mkielg11

Date: 15-06-2020

"""

import ctypes
from glob import glob


def _get_cdll_path(libname, file_suffix='.pyd'):
    return glob('../build/*/'+libname+'*'+file_suffix)[0]


def xpackage_function():
    xlib = ctypes.cdll.LoadLibrary(_get_cdll_path('xclib'))

    get_magic_number_func = xlib.return_magic_number
    get_magic_number_func.restype = ctypes.c_int

    return get_magic_number_func()


if __name__ == '__main__':
    print('Example package python file')
    print('Result of example package function:', xpackage_function())
