""" Write a program which accepts a sequence of comma-separated numbers from console and
generates a list and a tuple which contains every number in the form of string. """

values = input("Input some comma seprated numbers : ")
print(type(values))
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)