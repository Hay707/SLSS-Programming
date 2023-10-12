# Loop Practice
# Author: Hayley
# October 10 2023

# Create a list of groceries
groceries = ["hot wheels", "lego", "ice cream", "video games"]

# Do something for each thing in the list
# Print it out in a pretty way
#  e.g. * hot wheels
#         ---
#       * lego
#         ---

for item in groceries: 
    print(f"* {item}")
    print(" ---")
          
# Create a pyramid like this using a for loop

# *
# *
# ***
# ****
# *****

stars = ["*", "**", "***", "****", "*****"]

for row in stars: 
    print(f"{row}")



# Problem
 # Create a new years eve countdown
 # Requirements
 # * Starts off at 10  
 # * Countdown every second amd print the second that it's at
 # * Instead of reaching zero it says "Happy New Year"
 # Example Output: 
 #   10 
 #    9
 #    8
 #    ...
 #    1
 # "Happy New Year!"

import time

countdown = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "Happy New Year!"]

for seconds in countdown: 
    print(f"{seconds}")
    time.sleep(1)


  
