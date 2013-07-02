#coding:utf-8

from PIL import Image
from numpy import *
import imtool

filename = "lena.png"

im = array(Image.open(filename).convert('L'))
im2, cdf = imtool.histeq(im)
