""" Write a program in Python to multiply the elements of a list by itself using a traditional function
and pass the function to map() to complete the operation. """

def multiplication(n):
    return n * n
  
# We double all numbers using map()
numbers = [1, 2, 3, 4,5,6,7,8]
result = map(multiplication, numbers)
print(list(result))