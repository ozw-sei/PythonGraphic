#coding:utf-8

import cv
import cv2


# monariza
mona = cv2.imread("mona.jpg")
# mask
mask = cv2.imread("mona_mask.jpg")
# background
bg = cv2.imread("bg.jpg")

cv.Copy(mona,bg,mask)

show()
