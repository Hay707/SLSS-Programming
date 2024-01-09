# Colour Helper
# Author: Hayley
# December 19 2023


def is_light(pixel: tuple) -> bool: 
    """
    Takes a tuple and returns a boolean to tell whether the pixel is light or dark

    Params:
    pixel = 3-tuple of values (red, green, blue)

    Returns:
    True or False"""

    # red = pixel[0]
    # green = pixel[1]
    # blue = pixel[2]

    # average = (red + green+ blue) / 3

    # if average >= 128:
        # return True
    # else: return False
    # return sim(pixel) / len(pixel)

    if pixel >= (128, 128, 128):
        pixel = True 
    else: pixel = False

    
    return pixel


light_pixel = (255, 255, 255)
light_gray = (128, 128, 128)
darker_gray = (100, 128, 128)
dark_gray = (127, 127, 127)
dark_pixel = (0, 0, 0)

print(is_light(light_pixel))  # True
print(is_light(light_gray))   # True
print(is_light(darker_gray))
print(is_light(dark_gray))    # False
print(is_light(dark_pixel))   # False

# Colour Helper
# Functions that help wither colours

def pixel_to_gray_scale(pixel: tuple) -> tuple:
    """ Return a gray cersion of the given pixel"""
    red, green, blue = pixel

    gray = int(red * 0.31 + green * 0.59 + blue * 0.11)

    return (gray, gray, gray)

print(pixel_to_gray_scale((100, 34, 200)))

def pixel_to_random_effect(pixel: tuple) -> tuple: 
    """Return a random pixel"""
    red, green, blue = pixel 

    red += 30
    green += 50
    blue -= 10        # some random numbers

    if red > 255: 
        red = 255
    if green > 255:
        green = 255
    if blue < 0: 
        blue = 0


# Images Problem
# Author: Ubial
# 18 December 2023

from PIL import Image

import colour_helper

# Test?
light_pixel = (255, 255, 255)
light_gray = (128, 128, 128)
darker_gray = (100, 128, 128)
reddish_pixel = (255, 100, 24)
dark_gray = (127, 127, 127)
dark_pixel = (0, 0, 0)

print(colour_helper.is_light(light_pixel))  # True
print(colour_helper.is_light(light_gray))  # True
print(colour_helper.is_light(reddish_pixel))  # False
print(colour_helper.is_light(dark_gray))  # False
print(colour_helper.is_light(dark_pixel))  # False


def binarize() -> None:
    """Binarizes an image"""

    # Open the image
    with Image.open("./Images/catto.png") as im:
        image_height = im.height
        image_width = im.width

        # starting at the top and working our way down
        # visit the pixels from left to right
        for y in range(image_height):
            for x in range(image_width):
                pixel = im.getpixel((x, y))

                # if the pixel is light
                if colour_helper.is_light(pixel):
                    im.putpixel((x, y), light_pixel)
                else:
                    im.putpixel((x, y), dark_pixel)

        # After visiting every pixel, save the image
        im.save("./Images/binarized.jpg")




def picture_to_grayscale(filename: str) -> None:
    """Convert a given picture to grayscale"""

    # Open up the image
    with Image.open(f"./Images/{filename}") as im:
        # Visit every pixel
        for y in range(im.height):
            for x in range(im.width):    
                pixel = im.getpixel((x, y))
                
                # Take that pixel and convert it to gray
                random_pixel = colour_helper,pixel_to_random_effect(pixel)


                im.putpixel((x, y), random_pixel)
        
        # Save the image
        im.save("./Images/grayscale.jpg")


def pixel_to_name(pixel: tuple) -> str:
    """Given a 3-tuple, return a string representing
    its colour

    Params:
        pixel = 3-tuple of values (red, green, blue)

    Returns:
        name of the colour
    """
    red, green, blue = pixel

    # TODO: detect redpixels
    # red pixels -- r > 170, g> 60, b > 60
    if red < 200 and blue < 200 and green > 220:
        return "green"
    elif red > 170 and green < 60 and blue < 60: 
        return "red"
    else:
        return "colour unknown"
    
print(pixel_to_name((180, 3, 2)))
print(pixel_to_name((255, 255, 255)))