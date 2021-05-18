# Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().

from functools import reduce
x=reduce(lambda x,y:x+y,[1,2,3,4,5,6,7])
print(x)