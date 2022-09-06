# We are creating a calculator app that currently adds up two numbers "floats" that the user inputs
# and sums them up. Then it displays the sum.
# To-do: make the input invalid print statement re-loop.

print("Welcome to the Super Calculator!!")

def calculator():
    first_num = float(input('Please enter your first number: '))
    print(first_num)
    second_num = float(input('Please enter your second number: '))
    print(second_num)
    operation = str(input('Input one of the following; +, -, * or /?: '))
    if operation == '+':
        print(first_num + second_num)
    elif operation == '-':
        print(first_num - second_num)
    elif operation == '*':
        print(first_num * second_num)
    elif operation == '/':
        print(first_num / second_num)
    else:
        print('Input invalid, please select one of the following symbols: +, -, * or /')
        calculator()

while True:
    calculator()
