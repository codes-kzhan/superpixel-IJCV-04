from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import numpy as np
from ctypes import c_int, c_ubyte, c_float, cdll, POINTER

_segment_py_lib = cdll.LoadLibrary(
    os.path.join(os.path.dirname(__file__), 'segment_py.so'))
_segment_py_lib.segment_py.argtypes = [
    c_int, c_int, POINTER(c_ubyte), c_float, c_float, c_int, POINTER(c_ubyte)]
_segment_py_lib.segment_py.restype = c_int


def segment_img(img, sigma=0.5, k=500, min_size=20):
    assert img.dtype == np.uint8 and img.ndim == 3 and img.shape[-1] == 3
    h, w = img.shape[:2]

    # make a copy for modification
    img = np.ascontiguousarray(img, np.uint8)
    result = np.zeros_like(img)
    _segment_py_lib.segment_py(
        c_int(w), c_int(h), img.ctypes.data_as(POINTER(c_ubyte)),
        c_float(sigma), c_float(k), c_int(min_size),
        result.ctypes.data_as(POINTER(c_ubyte)))
    return result
