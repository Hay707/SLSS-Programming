# Olympic Judging
# Author: Hayley
# November 2 2023

# Write an Olympic Judging program that outputs 
# the average scores from 5 different judges
# Each score is out of 10 pints maximum
# Half points are allowed (eg. 7.5)
# The programs should take 5 input and output the final average

# Greet the user to the olympics
print("Welcome to the olympics! Here are the judges scores...")

scores = [
    "Judge 1:",
    "Judge 2:",
    "Judge 3:",
    "Judge 4:",
    "Judge 5:"
]

total_rating = 0

# Get judges rating 
for score in scores: 
    judges_score = int(input(score).strip(".,?!"))   

# Add score together for total rating 
    total_rating += judges_score

# Do some math on the results
# Use the average score to represent the judge rating
    average_score = total_rating/len(scores)

# Present the results
print(f'Your Olympic score is {average_score:.1f}/ 10')

