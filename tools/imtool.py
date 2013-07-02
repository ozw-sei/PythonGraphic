#coding:utf-8

import os


def get_imlist(path):
    '''指定したパスのjpgをすべて取得'''
    return [os.path.join(path, f)
            for f in os.listdir(path) if f.endswith('.jpg')]


def imresize(im, sz):
    """PILを使用して画像配列のサイズを変更する"""
    pil_im = Image.fromarray(uint8(im))
    return array(pil_im.resize(sz))


def histeq(image, nbr_bins=256):
    '''グレースケール画像のヒストグラム平坦化'''
    #画像のヒストグラムを得る
    imhist, bins = histgram(image.flatten(), nbr_bins, normed=True)

    #累積分布関数
    cdf = imhist.custom()

    #正規化
    cdf = 255*cdf/cdf[-1]

    # cdfを線形補間して、新しいピクセル値とする
    im2 = interp(image.flatten(), bins[:-1], cdf)

    return im2.reshape(im.shape), cdf
