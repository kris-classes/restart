def printCategory(age):
    print (" Value of age inside the function : ", age)
    if age > 18  and age <= 60:
        print('Adult')
    elif age > 65:
        print('Senior Citizen')
    else:
        print('Child')

age = int(input("\n Please enter the age : "))

print ("Value of age : ", age + 40)
print ("Value of age after addition : ", age)


printCategory(age)
