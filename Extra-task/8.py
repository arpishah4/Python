""" 8. Write a program in Python to complete the following task:
Create two lists such as even_list and odd_list
Ask user to enter a number in the range of 1,50 and make sure if the entered number is
even, append it to the even_list and if the entered number is odd append it to the odd_list.
Keep that in mind you can only add 5 items in each list
Make sure once you enter all the 5 elements, calculate the sum of the list and return the
maximum of the list. """


NumList = []
Even = []
Odd = []

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of Element : "))
    NumList.append(value)
    #print(NumList)
for j in range(Number):
    if NumList[j] % 2 == 0:
            size=len(Even)
            if size<=4:
             Even.append(NumList[j])
    else:
            size=len(Odd)
            if size<=4:
             Odd.append(NumList[j])

print("Element in Even List is : ", Even)
SumEven=sum(Even)
Maxeven=max(Even)
Maxodd=max(Odd)
print("Sum for Even list is:", SumEven)
print("Element in Odd List is : ", Odd)
print("Maximum element for Even list is:", Maxeven)
print("Maximum element for Odd List is : ", Maxodd)
SumOdd=sum(Odd)
print("Sum of Odd List is:",SumOdd)
