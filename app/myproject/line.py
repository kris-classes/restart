
var = input("Enter a line: ")
c=0
for i in var:
    if(i.isspace()):
        c+=1

if c==0:
    print("There are no spaces")
else:   
    print("Number of spaces : "+ str(c))  