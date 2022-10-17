#this game is a game chance
#game of chance

#ask user for their name
from multiprocessing import parent_process
from typing import ParamSpecArgs


name = input("Hi, whats your name? ")

print("Hi " + name)

#print the rules
print("This is how you play rock, scissors, paper")
print("You need to play with an apponent, I'll play with you")

#choose paper or rock or scissors
print("choose rock scissors paper")
print("rock kills scissors")
print("scissors kills paper") 
print("paper kills rock")

choice = input("Rock, scissors or paper")
print("You chose " + choice)
#check if user guessed correctly

#if they did then print Congradulations
#otherwise print sorry you lose, pay up
