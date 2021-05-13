""" 11. In the previous question, insert break after the “Good guess!” print statement. break will terminate
the while loop so that users do not have to continue guessing after they found the number. If the user
does not guess the number at all, print “Sorry but that was not very successful”.

 """
import random
guessesTaken = 1
number = random.randint(1, 20)
print(number)
#print('Well  I am thinking of a number between 1 and 20. :')
#guessnumber=int(input("Enter your Guess Number: "))
while guessesTaken<=4:
    print(guessesTaken)
   # print('Well  I am thinking of a number between 1 and 20. :')
    guessnumber=int(input("Enter your Guess Number: "))
    if number==guessnumber:
        print("Good Guess")
        break
    else:
        print("Try Again")
        guessesTaken+=1
        continue
if guessesTaken==5:
    print("Sorry but that was not successful")



