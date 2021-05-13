""" 9. Read the two parts of the question below:
Write a program such that it asks users to “guess the lucky number”. If the correct number is
guessed the program stops, otherwise it continues forever.

Modify the program so that it asks users whether they want to guess again each time. Use two
variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
The program continues as long as a user has not answered “no” and has not guessed the correct number) """

import random
number=random.randint(1,10)
print(number)

while True:
    guess=int(input("Enter the guess number"))
    if guess!=number:
     print("Try again")
     answer=input("Do you want to continue?")
     if answer=='YES':
         continue   
    
    if guess==number:
        print("Success")
        break



     
    
    



"""FIRST PART """
""" secret_number=10
number=int(input("Guess The Lucky Number :"))
print(number)
while secret_number != number:
    number = int(input('Guess a number until you get it right : '))
print('Well guessed!') """

""" secret_number=10
number=int(input("Guess The Lucky Number :"))
while secret_number != number:
    print("Your guess is not right")
    answer=input("Enter the Answer do you want to continue?Yes/No:")
    if answer=='Yes':
        number = int(input('Guess a number until you get it right : '))
print('Well guessed!')
 """

""" SECOND PART
number = -1
again = "yes"
while number != 5 and again != "no":
    number = input("Guess the lucky number: ")
    if number != 5:
        print (input("Would you like to guess again? "))
"""


