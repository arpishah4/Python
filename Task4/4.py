""" 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
in a hyphen-separated sequence after sorting them alphabetically. """

input=print(input("Enter the hyphen seperated list: "))
items=[n for n in input().split('-')]  
items.sort()  
print('-'.join(items))
print(items)