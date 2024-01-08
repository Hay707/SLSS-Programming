# Winter Holiday Review
# Author: Ubial
# January 8 2024

# Requirements:
# - create a function called winter_holiday()
# - take one parameter
#       - string
# - return a summary of a event from your holidays

import random


def winter_holiday(good_or_bad: str) -> str:
    """Give a summary of our winter holidays 2023/2024

    Params:
        good_or_bad - indicate what kind of event to summarize
        
    Returns:
        an event that happened during the holidays
        the event is selected randomly""" 
    


    good = [
        "I got to sleep in for many hours",
        "I ate lobster",
        "I got to spend time with my cousins",
        "I got the dundun chicken from miniso for Chirstmas"
    ]

    bad = [
        "I had to witness the lobsters getting cooked",
        "I had to do some physics homework"
    ]
     
    if good_or_bad == "good":
        return random.choice(good)
    elif good_or_bad == "bad": 
        return random.choice(bad)


def main() -> None:
    good_or_bad = input("Good or bad?")
    print(winter_holiday(good_or_bad))


if __name__ == "__main__":           # if dunder name == dunder main -> describes hidden properties in code 
    main()
        


