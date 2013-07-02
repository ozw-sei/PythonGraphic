#coding:utf-8
#
import numpy
from PIL import Image

pilIN = Image.open("hoge.jpg").convert("L")
imgArray = numpy.asarray(pilIN)
print imgArray
maxcol , maxrow = pilIN.size
imgArray.flags.writeable = True
for i in range(maxrow):
    for j in range(maxcol):
        if(imgArray[i,j] > 128):
            imgArray[i,j] = 1
        else:
            imgArray[i,j] = 0
pilOUT = Image.fromarray(numpy.uint8(imgArray))

pilOUT.show()

pilOUT.save('LLL.jpg')