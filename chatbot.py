# Chatbot
# Author: Hayley
# Date September 25 2023

# Put imports under header
import random
import time 

# Greet the user
# Pause in between lines of dialogue
print("Hello there!")
time.sleep(1.5)
print("I'm a crude chatbot, here to talk to you.")
time.sleep(1.5)

# Get the user's name and store in a variable
user_name = input("What's your name?")
time.sleep(1)

# Respond with the users name
print(f"It's nice to meet you, {user_name}!")

# Ask the user what their favourite food is
fave_food = input("What's your favourite food?")

# Respond with something that is NOT TOO repetitive
# Create a list of appropriate responses
list_of_fave_food_responses = [
    "Mmmmmm. That sounds delicious.",
    f"Wa!{fave_food} sounds good.",
    "RAH!!!",
    "Cool!"
]

# Choose one response randomly frmo the list

random_response = random.choice(list_of_fave_food_responses)
# Print out the random response
print(random_response)

