# Cookies
# Author: Hayley
# 21 November 2023

import turtle

# Make baker turtle
baker_turtle = turtle.Turtle()
baker_turtle.color("brown")

# Draw outline of cookie
baker_turtle.penup()             # take pen off canvas
baker_turtle.goto(5, -30)       # places on the "canvas"
baker_turtle.pendown()           # PUT pen down to start drawing
baker_turtle.circle(30)
baker_turtle.penup()

# Add 5 chips
baker_turtle.color("black")

baker_turtle.goto(0, 0)
baker_turtle.stamp()

# Top-right chip, bottom-right, bottom-left, top-left
baker_turtle.goto(10, 10)
baker_turtle.stamp()
baker_turtle.goto(10, -10)
baker_turtle.stamp()
baker_turtle.goto(-10, -10)
baker_turtle.stamp()
baker_turtle.goto(-10, 10)
baker_turtle.stamp()



turtle.done()