# Create a function that takes a list and returns a new list with unique elements of the first list.


def unique(list1):
 
    # intilize a null list
    unique_list = []
     
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    print(unique_list)
     

list1 = [10, 20, 10, 30, 40, 40,20,70,80,20,80]
print("the unique values from 1st list is")
unique(list1)
 
 
