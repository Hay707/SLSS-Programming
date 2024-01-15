# Robot Puppy Ball
# Author: Hayley
# January 12 2023

from PIL import Image

import colour_helper
import math

# ball colour
WHITE_PIXEL = (255,255,255)
BLUE_PIXEL = (0, 0, 255)

# Convert Image to a variable
robot_ball_img = Image.open("./Images/Red Ball.jpeg")

red_pixel_ball = []       # store the pixel of a ball

# Get all the pixels from the image
for y in range(robot_ball_img.height):
    for x in range(robot_ball_img.width):
        # Get the pixel information
        current_pixel = robot_ball_img.getpixel((x,y))
        # Store information of the colour of the ball to find the middle of the ball
        if colour_helper.pixel_to_name(current_pixel) == "red ball":
            # Store the placement of the ball somewhere
            red_pixel_ball.append((x,y))  

# Create a map of all red pixels "found"
# Create a new image that stores the map of the ball
#   - new image should be the same size as original
orig_image_width = robot_ball_img.width
orig_image_height = robot_ball_img.height

ball_pixel_map = Image.new("RGB", (orig_image_width, orig_image_height))

# save image

# Find all the red pixels in the ball and convert list into float to find radius of ball 
# and get the point 
ball_pixel_count = len(red_pixel_ball)

#center_of_ball = red_pixel_ball / 2


# ---

print(red_pixel_ball)

# ---

radius_of_ball = math.sqrt(ball_pixel_count / 3.14)

# For every pixel location in the radius of the ball
        # Place a white pixel (255, 255, 255) at that location
for pixel_loc in red_pixel_ball: 
    ball_pixel_map.putpixel(pixel_loc, WHITE_PIXEL)   # Takes two arguments -> varibale and colour pixel

num_of_coordinates = len(pixel_loc)

# find middle coordinate or center of the ball by taking all the 
# x coordinates and y coorinates and seperately divide it by 2
for y in pixel_loc: 
    # add all y coorindates and divide it by the amount of y pixels in pixel location
    y / num_of_coordinates

# do the same things as y but instead do x coordinate
for x in pixel_loc:
    x / num_of_coordinates

center_of_ball = (x,y)


# pixel_loc = the new x and y coordinate and print that coordinate out with a new colour
for center_of_ball in red_pixel_ball: 
    ball_pixel_map.putpixel(center_of_ball, BLUE_PIXEL)   # Takes two arguments -> location of ball and the colour that will indicate pixel

ball_pixel_map.save("./Images/Middle of Ball.jpg")


# Close file
robot_ball_img.close()

# did not work...

