# McDoland's Order
# Author: Hayley
# November 3 2023

# Write a McDoland's program that takes your order and outputs the total cost
# It first asks if you want a burger for $5.
# It then asks if you want fries for $3. It outputs the total with 14% tax
#The program should accept Yes/No or yes/no

# Greet the user before they order 
print("Hello! Welcome to McDoland's")

total_cost = 0
# Ask user they want a burger for $5
# If they say no, don't add $5 to their total
burger = input("Would you like a burger for $5?" + "\n")

if burger.lower() == "yes": 
    total_cost += 5
else: total_cost += 0

# Ask user if they want fries
# If they say no, don't add $3 to their total
fries = input("Would you like fries for $3?" + "\n")

if fries.lower() == "yes": 
    total_cost +=3
else: total_cost += 0

# Calculate final price with 14% tax
total_cost = total_cost + (total_cost * 0.14)

# Print final price
print(f"Your total is {total_cost:.3}")
