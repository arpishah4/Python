""" Write a program in Python using generators to reverse the string.
Input String = “Consultadd Training” """

str="Consultadd Training"

def reverse_string(my_str):
    length = len(my_str)
    for i in range(length-1, -1, -1):
        yield my_str[i]

# using for loop to reverse the string
for char in reverse_string(str):
    print(char)