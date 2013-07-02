#coding:utf-8
from PIL import Image
from pylab import *


if __name__ == "__main__":
    #画像を配列に読み込む
    im = array(Image.open('ozawa.jpg').convert('L'))

    #新しい図を作成
    figure()

    #Grayすけーる
    gray()

# 左上隅を原点とする等高線を表示
    contour(im, origin='image')
    axis('equal')
    axis('off')

    figure()
    hist(im.flatten(), 128)
    show()
