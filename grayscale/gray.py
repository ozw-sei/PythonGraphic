#coding-utf-8
from PIL import Image
from PIL import ImageOps

if __name__ == "__main__":
    input_img = Image.open("lena.png")
    output_img = ImageOps.grayscale(input_img)
    output_img.save("gray_lena.png")

def test():
    pass

