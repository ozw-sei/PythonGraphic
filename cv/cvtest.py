#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2

im = cv2.imread('lena.png')

h, w = im.shape[:2]

print h, w

cv2.imwrite('result.png', im)
