# Bubble Tea Poplar Algorithm
# Author: Hayley
# Date: October 27 2023

# Ask 5 users what theire favourite bubble tea place is
# Print out a summary of the data

NUM_RESPONDENTS = 5

coco_likes = 0
chatime_likes = 0
suntea_likes = 0
xingfutang_likes = 0
bbqueen_likes = 0

for _ in range(NUM_RESPONDENTS): 
        
    # Ask the user what their favourite bbt place is 
    print("What's your favourite bubble tea place?")
    fave_bbt = input().strip(",.?").lower()

    # Tallying/Counting Algorithm
    # Options: Coco, Chatime, Sun Tea, Xing Fu Tang, Bubble Queen
    # If they say Coco, increase the counter by one
    if fave_bbt == "coco": 
        coco_likes = coco_likes + 1
    elif fave_bbt == "chatime": 
        chatime_likes += 1            # short operand, increasing the chatime + gets one
    elif fave_bbt == "suntea": 
        suntea_likes += 1 
    elif fave_bbt == "xingfutang":
        xingfutang_likes += 1
    elif fave_bbt == "bbqueen": 
        bbqueen_likes += 1

# Print a summary of the results
print(f"Coco Likes: {coco_likes} | {coco_likes/NUM_RESPONDENTS * 100}%")
print(f"Chatime Likes: {chatime_likes} | {suntea_likes/NUM_RESPONDENTS * 100}%")
print(f"Suntea Likes: {suntea_likes} | {chatime_likes/NUM_RESPONDENTS * 100}%")
print(f"XingFuTang Likes: {xingfutang_likes} | {xingfutang_likes/NUM_RESPONDENTS * 100}%")
print(f"Bbqueen Likes: {bbqueen_likes} | {bbqueen_likes/NUM_RESPONDENTS * 100}%")

print("Thank you for participating in the BBT survey")