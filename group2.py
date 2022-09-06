#ride the bus, solo game. 
#guess red or black

# To-do implement the random selection the computer makes and match with user input
# print out whether the user has won or lost
import random

red_cards = list(range(1, 14))* 2
black_cards = list(range(1, 14))* 2
black_cards = random.shuffle()

print("Red or Black?")
user_red_input = int(input("Choose a number between 1-14 for a red card"))

if(user_red_input < 0 or user_red_input > 14):
    print("Card out of index")
else:
    print(f"You picked a red {user_red_input}")

# user_black_input = int(input("Choose a number between 1-14 for a black card"))
firstvalue = 
if(user_red_input < 0 or user_red_input > 14):
    print("Card out of index")
else:
    print(f"You picked a black {user_red_input}")
