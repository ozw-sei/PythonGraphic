# coding:utf-8

import sys
import cv2
import numpy as np



# 画像読み込み
try:
	filename = sys.argv[1]
except:
	filename = 'lena.png'

im = cv2.imread(filename)
im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
height,width = im.shape[:2]

# 塗りつぶし
diff = (6,6,6)
mask = np.zeros((height+2,width+2),np.uint8)
cv2.floodFill(im,mask,(10,10),(255,255,0),diff,diff)

#結果を保存
cv2.imshow('floodfill',im)
cv2.waitKey()

# 書き出しファイル名
try:
	write_name = sys.argv[2]
except:
	write_name = 'result.png'



cv2.imwrite(write_name,im)

