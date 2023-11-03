# Chip Rater
# Author: Hayley
# November 2 2023

# Interview people about their perception of 
# the taste of potato chips. We will ask them
# a set of questions. In the end, we'll give an
# aggregate score. 

# Greet the user (being frienly as possible lol)
print("Please answer the following questions on the chip you just ate. :)")

# Create a list of questions to ask
questions = [
    "How crispy is the chip on a scale on 1 to 5? 5 is very crispy, 1 is mushy",
    "How would you rate the taste from 1 to 5? 5 is best chip ever. 1 is I'd rather not eat it",
    "From 1 to 5, how would you rate the packaging. 1 is someone got paid to put this together?" 
]

total_rating = 0

# For every question in that list: 
for question in questions:               # singular question
    # Get the user's rating
    user_rating = int(input(question + "\n").strip(".,?!"))           # converting string into number, \n = users answer will be on the next line
    
    # Add the rating to some total-rating 
    total_rating += user_rating 

# Do some math on the results
# Use the average score to represent the chip's rating
    average_rating = total_rating/ len(questions)        # len = length | so length of question

# Present the results
print(f'The average rating for this chip is: {average_rating:.2f}/ 5')     # put two decimal places for the float (:.2f)

