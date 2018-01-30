/*
Copyright (C) 2006 Pedro Felzenszwalb

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
*/

#include <cstdio>
#include <cstdlib>
#include <image.h>
#include <misc.h>
#include "segment-image.h"

extern "C" int segment_py(int width, int height, unsigned char* data,
      float sigma, float k, int min_size, unsigned char* result) {
  image<rgb> *input = new image<rgb>(width, height);
  memcpy(imPtr(input, 0, 0), data, width * height * sizeof(rgb));
  int num_ccs;
  image<rgb> *seg = segment_image(input, sigma, k, min_size, &num_ccs);
  // copy the results back to the result array
  memcpy(result, imPtr(seg, 0, 0), width * height * sizeof(rgb));
  delete input;
  delete seg;
  return num_ccs;
}
