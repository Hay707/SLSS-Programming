# Functions Practice
# Author: Hayley
# November 24 2023

def print_area_of_a_square(sidelength: float) -> None:  # None doesn't expect the code to return a value
    """Calculates the area of a square.
    Results are in units squared.

    Params: 

    sidelength - length of one side of the square"""

    area = sidelength * sidelength
    
    print(f"The area of a square with side length = {sidelength} is: {area} square units")


def area_of_a_square(sidelength: float) -> float:
    """Returns the area of a square with given sidelength
    
    Params: 
    
    sidelength - length of one side of a square
    """
    area = sidelength**2      # raising to the power of 2

    return area                 # Returns function, takes function call with the value it returns

print_area_of_a_square(12.2)
print_area_of_a_square(13)
#sum_areas = area_of_a_square(12.2) + area_of_a_square(13)
print(area_of_a_square(2))
print(print_area_of_a_square(2))

# Question 1
# Define the function called stars and convert the interger into a string
# Have "*" represent a star
def stars(num_stars: int) -> str:
    """Takes the integer of the star and converts it into a string
    
    Params: 
    
    * - represents a star"""
  # Print the number of stars the user inputs  
    star = "*" * num_stars

    # print(star)
    
    return star

stars(3)
stars(10)
stars(5)

# Question 2
def biggest_of_three(num_one: int, num_two: int, num_three: float) -> float:
    """Takes three numbers given by the user and prints out the biggest value of the three numbers

    Params:

    num_one - first number
    num_two - second number
    num_three - third number 

    numbers = int"""

    # inputs 3 numbers

    biggest_number = 0

    numbers = [num_one, num_two, num_three]

    # For every number in the three numbers, if the number is greater than the biggest number,
    # that number becomes the biggest number

    for number in numbers:
        if number > biggest_number:
            biggest_number = number

    print(biggest_number)

    # prints out the biggest numbers
    return biggest_of_three

biggest_of_three(1,2,3)
biggest_of_three(1,8,7)

# Question 3
def pyramid(num_layers: int) -> str: 
    """
    Takes the integer of the number of stars and prints a row of the given integer
    
    Params:
    
    rows - number of layers
    "*" - represents a star"""

    star = "*"

    for rows in range(1, num_layers + 1):
        print(f"{rows * star}")
    
    return pyramid

pyramid(1)
pyramid(5)

# Question 4

def pyramid_mirror(num_layers: int) -> str:
    """
    Print a pyramid mirrored of given number of layers
    
    Params:
    num_layers - number of layers on the pyramid"""
    

    star = "*"
    space = " "
 # rows multiplied by the number of spaces which is the string then multiply it all for a sstinrg
    for rows in range(1, num_layers + 1):
        # Spaces is equal to total num of layers 
        # minus the stars in the current layer
        spaces = " " * (num_layers - rows)
        print(f"{spaces + stars(rows)}")

    return pyramid_mirror

pyramid_mirror(1)
pyramid_mirror(5) 