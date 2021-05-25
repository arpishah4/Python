""" 1. Write a program in Python to allow the error of syntax to be handled using exception handling.
HINT: Use SyntaxError """

try:
    print("I am in try block")
    a=input("Enter the expression:")
    z=eval(a)

except SyntaxError:
    print("Hi there is a syntax error")

else:
    print(type(a))
    print(z)