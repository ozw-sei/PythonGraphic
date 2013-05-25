from itertools import product
from PIL import Image
from PIL import ImageOps

def grayscale(input_image):
    width,height = input_image.size
    input_pixel = input_image.load()
    output_image = Image.new("L",(width,height))
    output_pixel = output_image.load()

    for x,y in product(range(width),range(height)):
        r,g,b = input_pixel[x,y]
        output_pixel[x,y] = (r + g + b)/3

    return output_image



if __name__ == "__main__":
    input_image = Image.open("lena.png")
    output_image = grayscale(input_image)
    output_image.save("gray_lena2.png")
