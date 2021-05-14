""" Write a program in Python to iterate through the string “hello my name is abcde” and print the
string which is having an even length. """

def printWords(s):
      
    # split the string 
    s = s.split(' ') 
    
      
    # iterate in words of string 
    for word in s: 
       
          
        # if length is even 
        if len(word)%2==0:
            print(word)
            
            
s = "hello my name is abcde" 
printWords(s) 