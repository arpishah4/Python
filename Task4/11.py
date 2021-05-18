""" Write a program which uses map() and filter() to make a list whose elements are squares of even
numbers in [1,2,3,4,5,6,7,8,9,10].
Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the
numbers in the filtered list. Use lambda() to define anonymous functions. """
#first use filter to find out the even elements

list1=[1,2,3,4,5,6,7,8,9,10]
filter_object=filter(lambda x:x%2==0,list1)
#print(list(filter_object))

list2=map(lambda y:y**2,filter_object)
print(list(list2))