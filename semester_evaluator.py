# Semester Evaluator
# Author: Hayley
# November 6 2023

# Create a Semester Evaluator Bot. 
# It ask how many courses you're taking this semester
# It takes the average rating of all the courses and gives a comment based on the average. 
# Score of 1 or lower. <score>? Ouch
# Score higher than 1 abu less than 3: <score>? Not a bad semester. 
# Score of 3 or higher. <score>? Glad to hear that!
# Probably use a for loop

# Ask how many courses they are taking
num_of_courses = input("How many courses are you taking?")

# Ask user to rate scale out of 5 based on the amount of courses they have. 
total_rating = 0


# Ask the rating questions
for i in range(int(num_of_courses)): 
    rating_question = f"How do you rate course {i+1} out of 5?"

    score = int(input(rating_question).strip(".,?!"))


    # Find the average score of users rating
    total_rating += score

average_rating = total_rating/int(num_of_courses)


# Print out final score for user response
if average_rating <= 1: 
    print(f"{average_rating:.2f}? Ouch.")
elif average_rating <= 3: 
    print(f"{average_rating:.2f}? Not a bad semester.")
else: print(f"{average_rating:.2f}? Glad to hear that!")

