# Pumpkin Drawing
# Author: Hayley 
# Date: 31 October 2023

# boiler code: "body" of code already set up

import turtle
import time

window = turtle.Screen()
window.bgcolor("black")

# Whole pumpkin
pumpkin = turtle.Turtle()
pumpkin.hideturtle()
pumpkin.color("orange")
pumpkin.dot(250)          # creates a bigger circle

# The turtle to "carve" the pumpkin
carver = turtle.Turtle()

# "Flatten" the lower part of the pumpkin
carver.penup()                  # you can see the line in front of the pic??
carver.setposition(-200, -100)
carver.pensize(50)
carver.pendown()
carver.forward(600)
carver.pensize(2)

# Nose
carver.penup()
carver.setposition(0, 0)
carver.dot(10)
carver.forward(15)
# carver.left(90)   # changes turtle so nose turns to the left

# Left Eye
carver.setpos(-50, 30)
carver.dot(30)

# Right Eye
carver.setpos(50, 30)
carver.dot(30)

# Mouth
carver.penup()
carver.setpos(-50, -50)
carver.pensize(5)
carver.pendown()
carver.forward(100)
carver.pensize(1)

# Right Tooth
carver.pendown()
carver.begin_fill()
carver.lt(-120)
carver.fd(25)
carver.lt(240)
carver.fd(25)
carver.end_fill()

# Stem of Pumpkin
stem = turtle.Turtle()
stem.color("brown")
stem.penup()
stem.setpos(0, 150)
stem.pendown()
stem.begin_fill() 
stem.fd(40)
stem.rt(90)
stem.fd(40)
stem.rt(90)
stem.fd(40)
stem.rt(90)
stem.fd(40)
stem.end_fill()
stem.pensize(30)
turtle.done()


