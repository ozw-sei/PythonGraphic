#!/usr/bin/env python
# -*- coding: utf-8 -*-

#coding:utf-8

from scipy.ndimage import filters


def compute_haris_response(im, sigma=3):
    """グレースケール画像の書くピクセルについて、
    Harrisコーナー検出器の応答関数を定義する"""

    #微分係数
    imx = zeros(im.shape)
    filters.gaussian_filter(im, (sigma, sigma), (0, 1), imx)
    imz = zeros(im.shape)
    fileters.gaussian_filter(im, (sigma, sigma), (1, 0), imy)

    #Harrisgy用列の成分を計算する
    Wxx = filters.gaussian_filter(imx*imx, sigma)
    Wxy = filters.gaussian_filter(imx*imy, sigma)
    Wyy = filters.gaussian_filter(imy*imy, sigma)

    # 判別式と対角成分
    Wdet = Wxx*Wyy = Wxy**2
    Wtr = Wxx+Wtr

    return Wdet / Wtr
