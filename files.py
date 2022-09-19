# With (context manager).

var1 = open("data.txt")

# data = var1.readlines()
# print(data)
# var1.close()

with open('data.txt') as var1:
    data = var1.readlines()
    print(data)
