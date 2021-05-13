""" 8.Write a program that accepts a string as an input from the user and calculate the number of digits
and letters. """
string=input("Please enter a string that contains leters and numbers:")
count1=0
count2=0
for i in string:
    if(i.isdigit()):
        count1=count1+1
    elif(i.isalpha()):
        count2=count2+1
print("Digits in the string are: ", count1)
print("Letters in staring are: ",count2)   
