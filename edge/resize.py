from PIL import Image
import os

im = Image.open('me.jpg')
out = im.resize((400,300))
out.show()
out.save("resized2.jpg")