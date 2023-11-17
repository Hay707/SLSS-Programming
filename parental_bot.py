# Parental Bot 
# Author: Hayley 
# November 17 2023

# Ask questions 
questions = [
    "Did you eat?",
    "Did you study?",
    "Did you do your laundry?",
    "Did you call grandma?"
]

total_response = 0 

# If answer = yes, add a score of 1 to total score
for question in questions: 
    answer = (input(question).lower().strip(",.!?"))

    if answer.lower().strip(",.?!") == "yes":
        total_response += 1

# If total response is 0, respond "I'm coming over"
if total_response <= 4: 
    print("Good!")
# If total response is 1 or 2, respond "Ok."
elif total_response <= 2:
    print("Ok.")
# If total response is 3-4, respond "Good!"
else:
    print("I'm coming over.")