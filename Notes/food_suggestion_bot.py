# Food Suggestion Bot
# Author: Hayley
# October 6 2023

# A bot that asks the user what their favourite food is. 
# The bot identifies the type/genre/cuisine of the food 
# and offer a suggestion for a restuarant

import random
import time

# Introduce  the bot to the user
# Ask the user what their favourite food is
print("Hello, I am here to suggest a restaurant to you.")
time.sleep(1)
fave_food = input("To help me suggest a restaurant, tell me what your favourit food is.")
time.sleep(1)

# If they answer with an Italian dish
# Suggest an Italian restaurant
# List all the Italian dishes
# Add one more cusine/type/etc.
# Test it to see if it works
italian_food = ["pizza", "pasta", "canneloni", "tiramisu"]
japanese_food = ["sushi, udon, tempura, yakisoba, sahshimi, ramen, donburi"]

if fave_food.lower().strip("'.?")in italian_food: 
    print("I think that you might like Italian food.")
    time.sleep(1)
    print("I  suggest Bella Roma Italian Ristorante Richmond.")
    time.sleep(1)
    print("You can find the address below:")
    print("8386 Alexandra Rd. Richmond")
elif fave_food.lower().strip("`.?") in japanese_food:
    print("I think you might like japanese food.")
    time.sleep(1)
    print("I suggest Otaru Japanese Kitchen")
    time.sleep(1)
    print("You can find the address below:")
    print("8180 No 2 Rd")
else:
    print("Sorry I don't recognize your favourite food")
    print("My algorithm is still being worked on.")
    time.sleep(2)
    print("I can't offer a suggestion for you :(")