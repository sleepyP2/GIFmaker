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
    frames = []
    for index, time in enumerate(range(15)):
        for i in range(img.size[0]):               # Rows
            for j in range(img.size[1]):           # Columns
                rgb = img.getpixel((i, j))
                img.putpixel((i, j), incColor(rgb, 17))
        path = abs_path + r'\frames\frame' + str(index) + ".png"
        img.save(path)
        frames.append(Image.open(path))

    img.save('myGIF.gif',
             append_images=frames,
             save_all=True,
             duration=100,
             loop=0)
