# AOC Dya 1
# Author: Hayley
# November 30 2023

# There is one elf carrying the most calories, how many calories does the elf have?

# Create a list that holds all the calories of the elves

# Create a list to hold all calories of elves
elves = []       # empty list

# Open the file
with open("./aoc2022day1.txt") as f: 
    # Calories of the current elf
    current_cals = 0       # Assuming elf does not carry anything

    for line in f:          # interating over every line in the file
        # If there is something in the line (other than a number)
        if line.strip(): 
            current_cals += int(line.strip())     # string -> integer     
        else:              
            # dump current_cals into elves list
            elves.append(current_cals)
            # reset current_cals for next elves 
            current_cals = 0

print (elves)
print(max(elves))

sorted_elves = sorted(elves)
top_three = sorted(elves[-3:])
top_three_total = sum(top_three)
print(sum(sorted(elves)[-3:]))      # SORTED takes a list and goes from smallest to biggest

# -3: gives last three biggest number
# sum adds all the numbers in the list together






    


