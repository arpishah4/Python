# FIND THE LARGEST AND SMALLET NUMBER FROM THE GIVEN LIST

""" list=[1,5,90,85,45,67,32]
print("Smallest number in the list is:", min(list))
print("Largest number in the list is: ",max(list)) """
#Python program to find smallest
# number in a list
 
# creating empty list
list1 = []
 
# asking number of elements to put in list
num = int(input("Enter number of elements in list: "))
 
# iterating till num to append elements in list
for i in range(1, num + 1):
    ele= int(input("Enter elements: "))
    list1.append(ele)
print(list1)    
# print maximum element
print("Smallest element is:", min(list1))