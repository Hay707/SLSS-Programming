# SFUs Best - Similarity Score
# Author: Hayley
# November 10 2023 

# Load data from a dile
# "Read" in a meaningful way
# Link our Sim Score algrithm to the data

# Open the file
#with open("./data.csv") as f: 
   #print(f.readline())            # gives string that represetns first line of fata
    
    # The secon line of the csv file
    #print(f.readline())

# function opens up a file 
# . = seperationg from file name 
# / file name
# data.csv = file name 
# give f a "place to live" to keep the file open

# Create a "profile" of likes (to see how similar we are to someone)
#(fave places in SFU)
profile = [
    "Bubble world",
    "Chef Hung", 
    "Uncle Fatih's",
    "Guadalupe (MBC)",
    "Steve's Poke Bar"
]

# Initialize top score and their name
most_similar_score = 0
most_similar_name = ""         # Place holder if you don't know who the "name" is or string
least_similar_score = 6
least_similar_name = ""

with open("./data.csv") as f:  # Takes care of file
    # Throw awat the header
    header = f.readline()           # Don't need header variable 

    for line in f: 
        # Convert te string to a list
        current_likes = line.split(",")
    
        # Store the person's name
        current_name = current_likes[1]

        # Initialize the current sim score
        current_sim_score = 0

        for item in profile:    
            if item in current_likes: 
                current_sim_score += 1

        # Print the results from this line of data
        print(f"{current_name} - Score: {current_sim_score}")
        
        # Update the most similar person
        if current_sim_score > most_similar_score: 
            most_similar_score = current_sim_score
            most_similar_name = current_name

        if current_sim_score < least_similar_score: 
            least_similar_score = current_sim_score
            least_similar_name = current_name

print("Most similar person!")
print(f"{most_similar_name} - Score: {most_similar_score}")    # Checks for most similar person
    
print("Least similar person!")
print(f"{least_similar_name} - Score: {least_similar_score}")
    

 



