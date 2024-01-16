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

for song in drake_songs: 
    if float(song[-1]) >= 0.6:  
        print(song)



# Print out all songs that have a danceability of >= 0.6
