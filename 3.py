# 3. Swap two numbers using a third variable and do the same task without using any third variable.

""" x = 10
y = 50
temp = x
x = y
y = temp
 
print("Value of x:", x)
print("Value of y:", y) """

x=10
y=50
x,y=y,x
print("Value of x:", x)
print("Value of y:", y) 