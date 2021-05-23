""" Write a program in Python to find out the character in a string which is uppercase using list
comprehension. """

test_str="Learn Python At Consult Add Inc "
res = [char for char in test_str if char.isupper()]
print("The uppercase characters in string are : " + str(res))
