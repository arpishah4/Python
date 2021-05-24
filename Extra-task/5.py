""" Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the
string with their index. """

def reverse(s):
  str = ""
  for i in s:
      str = i + str
  return str

def vowels(string):
    chars=list(string)
   
    size=len(string)
    vowels=[]
    for i in range(len(string)):
        if chars[i] in ['a','e','i','o','u']:
            vowels.append(chars[i])
    print(vowels)       


s = "HelloWorld How are you?"
  
print ("The original string  is : ",end="")
print (s)
  
print ("The reversed string is : ",end="")
print (reverse(s))

rev_string=reverse(s)

print ("The reversed string with vowels is : ",end="")
print (vowels(rev_string))