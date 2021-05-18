""" Define a function which can generate and print a tuple where the values are square of numbers
between 1 and 20 (both 1 and 20 included). """

def my_function(n): 
    list1=[] 
    for i in range(1,n): 
        a=i*i 
        list1.append(a) 
    #print(list1)
    tuple1=tuple(list1)
    print(tuple1)
         
my_function(20) 



