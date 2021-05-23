""" 1. Write a program that calculates and prints the value according to the given formula:
Q= Square root of [(2*C*D)/H]
Following are the fixed values of C and H:
C is 50.
H is 30.
D is a variable whose values should be input to your program in a comma-separated sequence. """
import math

C=50
H=30
numbers = input("Provide D: ")
numbers = numbers.split(',')
#print(numbers)
result_list = []
for D in numbers:
    Q = round(math.sqrt(2 * C * int(D) / H))
    result_list.append(Q)

print(result_list)