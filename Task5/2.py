""" Write a program in Python to allow the user to open a file by using the argv module. If the
entered name is incorrect throw an exception and ask them to enter the name again. Make sure
to use read only mode. """

import sys

#argv is the command that accepts input from the user,in command line.

file_name=sys.argv[1]

try:
    if file_name=="2.py":
        print("File opening is successful")
        f=open("2.py","r")
        print(f.readlines())
    else:
        raise NameError

except NameError:
    print("You are in Except block coz file name is not correct")

