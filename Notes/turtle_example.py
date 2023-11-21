# Turtle Example
# Author: Hayley
# November 21 2023

import turtle    # imports its function so you can use it in the "main face"

# ---- CONSTANTS
TURTLE_MAGNITUDE = 20           # interpret uppercase variables too

# Create a turtle 
michaelangelo = turtle.Turtle()   # Capital on Turtle tells you its a class
# Taking the class to make the type "Turtle"

# Get some instructions from the user
print("""To give commands,type:
F - to go forward
L - to go left
R - to got right
B - to go backwards
Stop - to stop""")                # Tell turtle where to go

# Repeat the below code INDEFINITELY
done = False

while not done:                             # expecting code block/a repeat
    command = input("Where should I go?")   # controls the loop

# Based on those instructions, move the turtle on the screen
# If the user says stop, quit the loos
    if command in ["f", "forward"]: 
        michaelangelo.forward(TURTLE_MAGNITUDE)     # how many pixels turtle should move forward (20 pixels)
    elif command in ["l", "left"]:
        michaelangelo.left(90) 
    elif command in ["r", "right"]:
        michaelangelo.right(90)  
    elif command in ["b", "backward"]:
        michaelangelo.back(TURTLE_MAGNITUDE)     
    elif command == "stop": 
        done = True

turtle.done()

# control c quits the program/process of code