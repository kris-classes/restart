import mymodule

result = mymodule.graffiti()
print(result)
print("attempting to clean...")
try:
    mymodule.clean()
except mymodule.MyError:
    print("there was a error cleaning the camera T-1000's have been dispatched")
finally:    
    print("this always occurs")

    # Modules, Error Handling, Try/Except/Finally.