from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import numpy as np


def read_ppm(path):
    with open(path, 'rb') as f:
        prefix, w, h, UCHAR_MAX, img_bytes = f.read().split(maxsplit=4)
    assert prefix.decode() == 'P6'
    assert int(UCHAR_MAX) == 255
    img = np.frombuffer(img_bytes, dtype=np.uint8).reshape((int(h), int(w), 3))
    return img


def write_ppm(img, path):
    assert img.dtype == np.uint8 and img.ndim == 3 and img.shape[-1] == 3
    h, w = img.shape[:2]
    img_bytes = img.tobytes(order='C')
    UCHAR_MAX = 255
    with open(path, 'wb') as f:
        f.write('P6\n{} {}\n{}\n'.format(w, h, UCHAR_MAX).encode())
        f.write(img_bytes)


def img2spid(img):
    assert img.dtype == np.uint8 and img.ndim == 3 and img.shape[-1] == 3
    img = img.astype(np.int32)
    # each color represents a segment; convert color to integers
    sp_ids = img[..., 0] * 65536 + img[..., 1] * 256 + img[..., 2]
    # convert to continuous ids starting from 0
    unique_sp_ids = np.unique(sp_ids)
    sp_id_map = {c: n_c for n_c, c in enumerate(unique_sp_ids)}
    vfunc = np.vectorize(lambda x: sp_id_map[x])
    sp_ids = vfunc(sp_ids)
    return sp_ids
