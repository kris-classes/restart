
# this is a terminal progam to show a list of files
import os
print("Welcome to our terminal program")
while 1:
        cmd = input("$ ")
        if cmd == "quit":
                quit()
        elif cmd == "ls":
                print(os.listdir())
        elif cmd == "lsraw":
                print(os.popen("ls").read())
        elif cmd == "create_new_folder":
                folder_name = input("what is your folder name? ")
                os.popen("mkdir "  +str(folder_name)).read()
        else:
                print("command not understood")
