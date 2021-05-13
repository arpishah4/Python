""" Write a program in Python to perform the following operator based task:
Ask user to choose the following option first:
If User Enter 1 - Addition
If User Enter 2 - Subtraction
If User Enter 3 - Division
If User Enter 4 - Multiplication
If User Enter 5 - Average
Ask user to enter two numbers and keep those numbers in variables num1 and num2
respectively for the first 4 options mentioned above.
Ask the user to enter two more numbers as first and second for calculating the average as soon as the user chooses an option 5.
At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
 At a time a user can only perform one action. """

choice=int(input("Enter a number between 1 to 5: "))
if choice==1 or choice==2 or choice==3 or choice==4:
    x=int(input("Enter 1st number :"))
    y=int(input("Enter another number :"))
    if choice==1:
        result=x+y
        print(result)
    if choice==2:
        result=x-y
        print(result)
    if choice==3:
        result=x/y
        print(result)
    if choice==4:
        result=x*y
        print(result) 
    if result<0:
        print("Negative")
else:
    First= int(input("Enter First Number :"))
    Second=int(input("Enter Second Number :"))
    Total=First+Second
    Result=Total/2
    print(Result)
    if Result<0:
        print("Negative")
            


