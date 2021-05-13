""" 1. Write a program in Python to perform the following operation:
If a number is divisible by 3 it should print “Consultadd” as a string
If a number is divisible by 5 it should print “Python Training” as a string
If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a string """

Num1=int(input("Enter any number: "))
if Num1%3==0:
    print("Conultadd")
if Num1%5==0:
    print("Python Training")
if Num1%3==0 and Num1%5==0:
    print("Consultadd - Python Training")    