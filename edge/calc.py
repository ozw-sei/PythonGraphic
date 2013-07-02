# coding:utf-8

import cv2


#画像読み込み
im = cv2.imread('lena.png')

#グレースケール
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

#積分画像を計算
initim = cv2.integral(gray)

# 正規化
initim = (255.0 * initim) / initim.max()
cv2.imwrite('result.png',initim)


