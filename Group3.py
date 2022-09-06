# Grocery list - Interactive shopping list

print ("Hello there, welcome to this luxury shopping list")

my_list = ["Bread", "Milk", "Coffee"]
# User add an essential item (chocolate) then pop it

print(my_list)

while True:
    answer = input("Would you like to add to the shopping list? Y/N ")

    if answer == "Y":
        new_item = input("What would you like to add? ")
        my_list.append(new_item)
        print(my_list)
    elif answer == "N":
        answer2 = input("Would you like to remove an item from the list? Y/N ")
        if answer2 == "Y":
            old_item = input("What would you like to remove? ")
            my_list.remove(old_item)
            print(my_list)
        else:
            print(my_list)
            break
    else:
            print(my_list)
            break       
