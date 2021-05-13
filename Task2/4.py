"""
4.Write a program in python to break and continue if following cases occur: 
If user enters a negative number just break the loop and print “It’s Over”
If user enters a positive number just continue in the loop and print “Good Going”
 """
while True:
    i = input('Please enter number:\n')
    i = int(i)
    if i > 0:
        print("Good Morning")
        continue
    if i < 0:
        print("Its over")
        break
    
