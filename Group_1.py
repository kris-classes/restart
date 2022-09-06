'''
Calculator app that calculates result of two numbers from user and then loops
Asks user for two numbers
User then chooses what calculation they want to do
Calculator will output result and then loop to asking for user to input numbers
To-do:
    make the input invalid print statement re-loop, without asking for numbers again
'''

print("***** Welcome to the Super Calculator!! *****")

def calculator():
    #asks user for first number, then displays it
    first_num = float(input('Please enter your first number: '))
    print(first_num)
    #asks user for second number, then displays it
    second_num = float(input('Please enter your second number: '))
    print(second_num)
    #aks user for type of calculation
    print("What would you like to do?")
    operation = str(input('Input one of the following; +, -, * or /?: '))
    
    #calculates result and displays it
    if operation in ('+', '-', '*', '/'):
        if operation == '+':
            print(first_num, "+", second_num, "=", first_num + second_num)
        elif operation == '-':
            print(first_num, "-", second_num, "=", first_num - second_num)
        elif operation == '*':
            print(first_num, "*", second_num, "=", first_num * second_num)
        elif operation == '/':
            print(first_num, "/", second_num, "=", first_num / second_num)
    else:
        print('Input invalid')
                    
# keeps the calculator running/looping
while True:
    calculator()
