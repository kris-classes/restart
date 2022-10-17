

import random

# Roll the dice
# Enter the player name
player1 = input('Enter your name :')
print(player1)
dice = (1,2,3,4,5,6)
# Choose random number
randomdice = random.choice(dice)
print(randomdice)
print(f'The Player {player1} random dice number is {randomdice}')
