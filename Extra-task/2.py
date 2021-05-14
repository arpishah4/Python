# Create a list of thousand numbers using range and xrange and see the difference between each other

# Difference: The only difference is that range returns a Python list object and xrange returns an xrange object.
""" range() returns – range object.
xrange() returns – xrange() object.
 """

#initializing a with range()
a = range(1,1000)
  
# initializing a with xrange()
x = xrange(1,1000)
  
# testing the type of a
print ("The return type of range() is : ")
print (type(a))
  
# testing the type of x
print ("The return type of xrange() is : ")
print (type(x))