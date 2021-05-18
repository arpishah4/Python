""" Write a function that accepts a string and prints the number of uppercase letters and lowercase
letters. """



def upperlower(string):
    upper=0
    lower=0

    print("the string is ",string)
    for i in range(len(string)):
        if string[i].isupper():
            upper+=1
        else:
            lower+=1    
    print("Uppercase characters are: ",upper)        
    print("Lowercase characters are: ",lower)        



string="ABCDefghIJKLmnopqr"
upperlower(string)