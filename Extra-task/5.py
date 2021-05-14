""" Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the
string with their index. """

def reverse(s):
  str = ""
  for i in s:
      str = i + str
  return str

def vowels(str):
    str1=""
    vowels=set('aeiou')
    for char in str:
        if char in vowels:
            str1.add(char)
    return str1        


   


s = "HelloWorld How are you?"
  
print ("The original string  is : ",end="")
print (s)
  
print ("The reversed string is : ",end="")
print (reverse(s))

print ("The reversed string with vowels is : ",end="")
print (vowels(str))