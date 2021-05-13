
""" Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
such as

While counter <= 5:
print(“Type in the”, counter, “number”
counter=counter+1
The program asks for five guesses (no matter whether the correct number was guessed or not). If the
correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
After the fifth guess it stops and prints “Game over!”. print ("Game Over") """
   
import random
guessesTaken = 1
number = random.randint(1, 20)
print(number)
#print('Well  I am thinking of a number between 1 and 20.')
while guessesTaken <= 4:
    guess = int(input("Enter your guess number: "))
    if guess!=number:
        guessesTaken+=1
        print("Try Again")
    else:
        guessesTaken+=1
        print("Good Guess")
if guessesTaken>5:
    print("Game over")