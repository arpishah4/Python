""" Define a function that can receive two integral numbers in string form and compute their sum and
print it in the console. """

def calculateSum (a,b):
	s = int(a) + int(b)
	return s 

num1=input("Enter a number: ")
num2=input("Enter another Number: ")

# calculate sum
sum = calculateSum (num1, num2)

# print sum
print("Sum is: ", sum)