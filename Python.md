# Luke Notes
## Python language

Functions 1
Print()
Prints what is inside the brackets
Example: 
Print(“hello”)
Would output: 
Hello

Variables
Int (this is an integer  whole number (i.e 1, 12, 108))
Float (this is a floating point number, has a decimal point (i.e 1.2, 104.299, 22.7))
Bool (known as a boolean, an expression that returns either true or false)
String (anything between quotation marks, and alpha-numeric characters (ie a-z, 1-9, ?, etc)

Functions 2
type()
Returns type of variable between brackets
Example: type(1)
Would output: int
(“but remember it won't appear in the terminal unless is it stored inside a variable”)

Storing Variables
Name on the left then an equals sign then what that variable equals
Example 1: name = “Luke”
	print(name)

Outputs: Luke

Example 2: age = 42
	print(age)

Outputs: 100

Example 3
Can also add to stored variables
age = 42
age2 = age + 8
 
print(age)
print(age2)











Comments
Comments are denoted by a “#” at the beginning of a line, 
and basically tell the program to ‘skip this line’.
They can be helpful reminders, instruction, or intention, or complete nonsense

Example:
print(“bob”)
#bob smells
Output:
bob

“””
All between the 3 quotes are comments
“””

Input 
Asks the user to input some value. Could be a string, could be an int, float, etc
Example:
Input(“how old are you?”)
In this case the input will be returning a string.
10 as an input would still be considered a string

If, elif, else
if
If this thing is true then do this
Example:
If 1 != 1:
	print(not the same)

Example 2
answer = int(Input (“what is 1 + 1?”))
If answer == 2:
	print(“correct”)
Else:
	print(“better hit the books”)

*“answer” being a variable in this case

Example 3:
name = input("what’s your name? ")
if name == "John":
    print("hello John")
elif name == "Julia":
    print("hola Julia")
else:
    print("hello stranger")




Changing a variable's class
speed = input("Enter the car's speed? ")
speed = int(speed)
if speed >= 100:
    print("Your speed is " +str(speed) +" please slow down")
elif speed <= 50:
    print("Your speed is " +str(speed) +" please speed up")
else:
    print("Your speed is good at " +str(speed))
Changes the variables class from a string, to an int (to check against the if statement) then back to a string to print.

Symbols
= changes what is on the left to the right (equals this now)
== is the value of the left side of the symbols ‘is equal to’ the right? (“is equal two”) 
!= does not equal (the opposite of “is equal to”)
<= equal to or less than
>= equal to or greater than

