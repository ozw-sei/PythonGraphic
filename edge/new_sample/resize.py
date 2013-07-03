from PIL import Image
import os
import sys

try:
    filename = sys.argv(1)
except:
    filename = '5.jpg'

try:
    outfilename = sys.argv(2)
except:
    outfilename = 'out.jpg'

try:
    orientation = True
except:
    prientation = False

im = Image.open(filename)
if orientation is True:
    out = im.resize((400,300))
else:
    out = im.resize((300,400))
    
out.show()
out.save(outfilename)