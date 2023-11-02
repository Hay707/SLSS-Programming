# Age in 2049
# Author: Hayley
# November 2 2023

# Write an Age in 2049 program that asks your age and outputs 
# how old you'll be by then
import time

# Greet the user
print("hello there, I am here to see what age you'll be in 2049")
time.sleep(1)

# Ask the user how old they are
age_in_2049 = int(input("How old are you?"))

# Add their age by 26 years (2049-2023 = 26) and print their age is 2049
print(f"In 2049, you willl be {age_in_2049 + 26} years old")
