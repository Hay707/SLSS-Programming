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

for question in questions: 
    answer = (input(question).lower().strip(",.!?"))

    if answer.lower().strip(",.?!") == "yes":
        total_response += 1

if total_response == 0: 
    print("I'm coming over.")
elif total_response <= 2:
    print("Ok.")
else:
    print("Good!")