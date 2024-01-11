# Jelly Bean Colour Counter
# Author: Hayley 
# Jamuary 9 2024

# Version 0.1
# - Count red pixel/beans
# - Report on the percentage of all red beans 

from PIL import Image

import colour_helper

jelly_bean_img = Image.open("./Images/Jelly Beans.jpg")

red_pixels = []

# Visit every pixel in the image
for y in range(jelly_bean_img.height):
    for x in range(jelly_bean_img.width):
    # Get the pixel information
        current_pixel = jelly_bean_img.getpixel((x,y))

    # If the pixel is red
    if colour_helper.pixel_to_name(current_pixel) == "red":
       # Store its location somewhere 
        red_pixels.append((x,y))
# Count all the locations of red pixels
red_pixel_count = len(red_pixels)
total_pixels = jelly_bean_img.width * jelly_bean_img.height

# Divide by the total pixels in the image
red_pixel_percentage = red_pixel_count / total_pixels * 100

# Generate the report
print(f"Red Jelly Beans: {round(red_pixel_percentage, 2)}%")

jelly_bean_img.close()

