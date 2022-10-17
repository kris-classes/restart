#this game is a game chance
#Created by Kura 19/09/2022
#game of chance
import random
#ask user for their name
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

user_choice = input("Choose now rock, scissors or paper: ")
print("You chose " + user_choice)
#check if user guessed correctly
#make a guess from computer
options = ["rock", "scissors", "paper"]
computer_choice = random.choice(options)
print("The computer chose " + computer_choice)
#if they did then print Congradulations
#check for draw
if user_choice == computer_choice:
    print("both win and its a draw")

elif user_choice == "rock" and computer_choice == "scissors":
    print("Congradulations you win computer loses")

elif user_choice == "scissors" and computer_choice == "paper":
    print("Congradulations you win computer loses")

elif user_choice == "paper" and computer_choice == "rock":
    print("Congradulations you win computer loses")
else:
    print("Computer wins")
#otherwise print sorry you lose, pay up
print("Thanks for playing " + name)
