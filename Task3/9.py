""" Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
and n(both 1 and n included). """

n=int(input("Enter the number for dictionary :"))
dict1=dict()
for x in range(1,n+1):
    dict1[x]=x**2
print(dict1)