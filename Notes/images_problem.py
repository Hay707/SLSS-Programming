# Images Problem
# Author: Hayley
# DEcember 18 2023

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


# Test 
light_pixel = (255, 255, 255) 
light_gray = (128, 128, 128)
dark_gray = (127, 127, 127)
dark_pixel = (0, 0, 0)

print(is_light(light_pixel))  # True
print(is_light(light_gray))   # True
print(is_light(dark_gray))    # False
print(is_light(dark_pixel))   # False

# Open the image

# For every pixel in the image 
    # if the pixel is light
        # replace it with a light pixel
    # else 
        # replace it with a dark pixel 

from PIL import Image

with Image.open("./Images/catto.png") as im: 
        # create variable that store the width and height
    # visit the pixels from left to right
    image_height = im.height
    image_width = im.width

    # open background image
    # *** REMEBER TO CLOSE THE IMAGE WHEN DONE
    cat_im = Image.open("./Images/catto.png")
    # starting at the top and working our way down
    for y in range(image_height):
        for x in range(image_width):
            #print this pixels informaion
            pixel = im.getpixel((x,y))

            if pixel >= (128, 128, 128):
                im.putpixel((x,y), (255, 255, 255))
            else: im.putpixel((x,y), (0, 0, 0))
    cat_im.close()

    # Save image
    im.save("./Images/output.jpg")




with Image.open("./Images/best_pizza.jpg") as im:
    # create varibale with width and height 
    # visit the pixels from left to right
    image_height = im.height
    image_width = im.width
    
    # variables for colour
    light_pixel = (255, 255, 255)
    lightest_gray = (129,129,129)
    light_gray = (128, 128, 128)
    darker_gray = (100, 128, 128)
    dark_gray = (127, 127, 127)
    dark_pixel = (0, 0, 0)

    # set image to varible so there isn't much typing 
    pizza_im = Image.open("./Images/best_pizza.jpg")
    # starting at the top and working its way down the image
    for y in range(image_height):
        for x in range(image_width):
            pixel = im.getpixel((x,y))

            if is_light(pixel) == True: 
                if pixel >= (lightest_gray) and pixel < (lightest_gray):
                    im.putpixel((x,y),(light_pixel))
                else: im.putpixel((x,y), (light_gray))
            if is_light(pixel) == False: 
                if pixel >= (darker_gray) and pixel < (dark_gray):
                    im.putpixel((x,y), darker_gray)
                elif pixel >= (dark_gray):
                    im.putpixel((x,y), dark_gray) and pixel < (dark_pixel)
                else:
                    im.putpixel((x,y), dark_pixel)

    pizza_im.close()

    # save image
    im.save("./Images/output.jpg")




