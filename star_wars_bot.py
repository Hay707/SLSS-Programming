# Star Wars Bot
# Author: Hayley Chan
# October 16 2023

import time 

# Introduce the DARK SIDE INTERVIEW
# Make sure reader is able to read so give them enough time
print("I am here to decide if you can join the Dark Side")
time.sleep(2)
print("Let's begin >:)")
time.sleep(2)

# Ask user if their favourite colour is red
fave_colour = input("Is your favourite colour red")

# Ask user if they like capes
cape = input("Do you like capes?")
time.sleep(1)

# If user answers yes to both or one of the questions, 
# user is part of dark side
# If user answers no to both questions or types something random
# user is part of the light side
# User upper/lowercase answers must be included

if cape.lower().strip("'.?") == "yes" or fave_colour.lower().strip("'.?")== "yes": 
    print('You are part of the DARK SIDE!!')
else: print ("You are part of the Light Side :)")  