# World Traveller
# Author: Hayley 
# November 3 2023

# Create a World Traveller 
# It asks for the user's name and greets them. 
# Then it asks if the user has been to each of the continents
# After it finishes asking, it tells the user how many continents they've been to.
# Must you loops

# Ask for user's name and greet them
name = input("What's your name?" + "\n")
print(f"Hello {name}! It's nice to meet you")

# Ask user about what continents they've been to. 
questions = [
    "Have you been to Asia?",
    "Have you been to Europe?",
    "Have you been to North America?",
    "Have you been to South America",
    "Have you been to Australia?", 
    "Have you beem to Africa?",
    "Have you been to Anarctica?"
]

total_continents = 0
 
 # Get users response to see how many continents they've been to 
for continents in questions:
    # Ask the question
    # Get the answer
    answer = input(continents).lower().strip(",.!?")

    # If the answer is yes
    if answer == "yes": 
        total_continents += 1


# Print out user result for how many continents they've been to
print(f"I see, you've visited {total_continents}/7 continents!")