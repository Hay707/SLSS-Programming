# Similar Hobbies
# Author: Hayley
# November 14 2023


# Ask question
print("Please enter hobbies, separated by spaces.")

similarity_score = 0

# Ask person one what their hobbies are
person_one_hobbies = input("Person One: ")

for hobby_one in person_one_hobbies: 
    current_likes = hobby_one.split(" ")

# Ask person two what their hobbies are
person_two_hobbies = input("Person Two: ")
for hobby_two in person_two_hobbies: 
    current_likes = hobby_two.split(" ")

if hobby_two in person_one_hobbies: 
    similarity_score += 1

print(f"You have {similarity_score} in common!")










    

 



