# We are creating a calculator app that currently adds up two numbers "floats" that the user inputs
# and sums them up. Then it displays the sum.
# To-do, add other operation functions! Also ask user what operation they would like to do?
print("Calculator App...")
print("Lets add two numbers together!")
var_x = float(input("Type first number to be added..."))

var_y = float(input("Type second number to be added..."))
var_result = var_x + var_y
print(f"Your sum of {var_x} and {var_y} is {var_result}!")
