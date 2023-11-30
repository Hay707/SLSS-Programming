# File Exercises
# Author:
#

#"""Instructions:

#Put this file in your programming folder.
#Download the data-example.csv file and put it in this same folder.
#For each problem, design a solution.
#Each part builds on the previous step, so don't skip any.
#You can refer to the work that we did last day for any hints.
#Do not use any generative AI for the solutions."""

# Since our file has some symbols in it, this is the most
# effective way at opening up the file.

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()

# Note that I've set the encoding parameter to "utf-8"

# --- Problems


# Problem 1:
# Open the file and print the contents of the second line in the file.

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()    
    print(f.readline())

# Problem 2:
# Good! Now that you've done that, open the file, and print out every line of data.
with open("./data_example.csv", encoding="utf-8") as f:
    for line in f: 
        print(line)

# Problem 3:
# If you've made it this far, well done. Next task:
# Convert that line of data into a list.
with open("./data_example.csv", encoding="utf-8") as f:
    for line in f: 
        print(line.split(","))

# Problem 4:
# Give yourself a pat on the back.
# See if you can count how many people like "Chicken Adobo" as their
# favourite food.
chicken_score = 0

with open("./data_example.csv", encoding="utf-8") as f:
    for food in f: 
        if food.split(",")[1] == "Chicken Adobo":
            chicken_score += 1

print(f"{chicken_score} people like Chicken Adobo!")
        
# Problem 5:
# You should have gotten four people for the last problem. If not,
# see if why your code doesn't work.
# Else, you can move on to this part, which is, find out how many
# people have the first letter of their first name start with "A".
a_name_score = 0

with open("./data_example.csv", encoding="utf-8") as f:
    for name in f: 
        # If the first name starts with the letter "A'"
        first_name = name.split(",")[0]
        first_name.split(" ")
        if "A" in first_name[0]:
            # Increase name score by 1
            a_name_score += 1
        
            
print(f"{a_name_score} people's name start with an A!")

# Problem 6:
# 19 people! Excellent. How many people come from Guangzhou?
guangzhou_score = 0

with open("./data_example.csv", encoding="utf-8") as f:
    for place in f: 
        # If people come from Guangzhou, increase guaungzhou score by 1
        if place.split(",")[4] == "Guangzhou\n":
            guangzhou_score += 1

print(f"{guangzhou_score} is from Guangzhou!")
        
# Problem 7:
# Just one is from Guangzhou! Alright, last one. How many people have a credit card
# number that is even. There are a couple of ways to solve this.
# You can either do this with the string or with the int.
even_credit = 0

with open("./data_example.csv", encoding="utf-8") as f:
    for credit in f: 
        # if all number contains 0,2,4,6,8, add score to people with even numbers
        if credit.split(",")[3] == [0,2,4,6,8]: 
            even_credit += 1

print(even_credit)

# Problem 8*:
# Sorry, no answer for the above one. This one is a challenge question.
# Can you design a way to find the most popular food?

# Put all food inside a list
# Don't know every food so it'll be labeled as " "

most_sim_food_name = " "
most_sim_food_score = 0

all_food_score = 0  
every_food_score = 0

all_food = [
    " "
]
# If food is in the list "all_food", food_score + 1
# If food is not in list food is added into list a
with open("./data_example.csv", encoding="utf-8") as f: 
   for every_food in f: 
        likes_of_food = every_food.split(",")
        # Store food into list
        food_name = likes_of_food[1]

        if every_food in all_food:
            all_food_score += 1
            every_food_score += 1
        elif every_food not in all_food: 
            every_food == " "
            every_food_score += 1

if every_food_score >= every_food_score: 
    most_fave_food = every_food

print(most_fave_food)