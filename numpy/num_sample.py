#!/usr/bin/env python
# -*- coding: utf-8 -*-

#coding:utf-8

from PIL import Image
from numpy import *

if __name__ == "__main__":
    im = array(Image.open('lena.png').convert('L'))

    #画像を反転
    im2 = 255 - im

    #100~200の値に縮める
    im3 = (100.0/255) * im + 100

    # 2乗する
    im4 = 255.0 * (im/255.0)**2
    print int(im.min()),int(im.max())
