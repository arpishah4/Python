# Write a program to get the sum and multiply of all the items in a given list.

# sum()
   
numbers = [1,2,3,4,5,1,4,5]
  
# start parameter is not provided
Sum = sum(numbers)
#print(Sum)
  
# start = 10
Sum = sum(numbers, 1)
#print(Sum)

#sum using function
def dosum(myList):
    result=0
    for x in myList:
        result=result+x
    return result
number=[1,2,3,4,5,6]
print(dosum(number))

def multiplyList(myList) :
     
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x
    return result
     
# Multiply code
numbers = [1, 2, 3,4,5]
#print(multiplyList(numbers))
