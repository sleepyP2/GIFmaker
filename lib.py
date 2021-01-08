# IMPORT
from PIL import Image
import os

# Get Absolute Path
abs_path = os.getcwd()


# Loads the image so there is no need to import Pillow in main.py
def load_img(img):
    return Image.open(img)


# Increment Color function to increment the rgb value
def incColor(color, increment):
    r = color[0] + increment
    
    # Check if the value is greater than 255
    if r > 255:
        r -= 255
    g = color[1] + increment
    if g > 255:
        g -= 255
    b = color[2] + increment
    if b > 255:
        b -= 255

    rgb = (r, g, b)

    return rgb


# Function to make a GIF
def rainbowGIF(img):
    for index, time in enumerate(range(15)):
        for i in range(img.size[0]):               # Rows
            for j in range(img.size[1]):           # Columns
                rgb = img.getpixel((i, j))
                img.putpixel((i, j), incColor(rgb, 17))
        img.save(abs_path + '\\frames\\frame' + str(index) + ".png")

    im1 = Image.open('frames/frame0.png')
    im2 = Image.open('frames/frame1.png')
    im3 = Image.open('frames/frame2.png')
    im4 = Image.open('frames/frame3.png')
    im5 = Image.open('frames/frame4.png')
    im6 = Image.open('frames/frame5.png')
    im7 = Image.open('frames/frame6.png')
    im8 = Image.open('frames/frame7.png')
    im9 = Image.open('frames/frame8.png')
    im10 = Image.open('frames/frame9.png')
    im11 = Image.open('frames/frame10.png')
    im12 = Image.open('frames/frame11.png')
    im13 = Image.open('frames/frame12.png')
    im14 = Image.open('frames/frame13.png')
    im15 = Image.open('frames/frame14.png')

    img.save('myGIF.gif',
             append_images=[im1, im2, im3, im4, im5, im6, im7, im8, im9, im10, im11, im12, im13, im14, im15],
             save_all=True,
             duration=100,
             loop=0)
