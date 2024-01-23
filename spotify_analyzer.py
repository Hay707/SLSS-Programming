# Spotify Data Analyzer
# Author: Hayley 
# Jan 16 2024

# Version 0.1 
#   - From the data set, get all the songs
#     performed by Drake 

import csv 

def find_all_songs(artist: str) -> list:
    """Returns a list of all songs sfrom a given artist."""
    # Open up the file 
    with open("./spotify.csv") as f: 

        # ---- Look for all songs performed by every artist
        #      Use linear search
        # Creat a csv reader object
        csv_reader = csv.DictReader(f)

        # Make a list to store all Drake's songs
        songs = []
        

        # For every song in the ,csv gile
        for line in csv_reader:
            # Check if it's the first line 
            if artist.lower() in line["artist"].lower():
                # add it to the Drake's song list
                songs.append(
                    (line["artist"], line["song_title"], line["danceability"])
                )
        return songs

drake_songs = find_all_songs("Drake")

# Print out all songs that have a danceability of >= 0.6
for song in drake_songs: 
    if float(song[-1]) >= 0.6:  
        print(song)

# --- Sorting Algorithm (lowerst to highest)
# --- Selection Sort

# Starting at the beginning of the list
for i in range(len(drake_songs)): 
        # Set the current item to te smallest value
        smallest_danceability = drake_songs[i][-1]   # i = different songs ; -1 = list at the end 
        # For the rest of the list 
        for j in range(i + 1, len(drake_songs)):         # + 1 to look at next number
            # Check to see if next number is smaller
            if drake_songs[j][-1] < smallest_danceability:
                # If number is, set that number to the smallest number
                smallest_danceability = drake_songs[j][-1]
                smallest_index = j
        
        # Swap the current position with the smallest nuber we found
        drake_songs[i], drake_songs[smallest_index] = drake_songs[smallest_index], drake_songs[i] 
        # Order matters

for song in drake_songs: 
    print(song)