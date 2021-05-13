"""Create a new list which contains the specified numbers after removing the even numbers from a
# predefined list."""

#Initialisation of list
list = [1,2,3,4,5]
  
# Output list initialisation
out = []
  
for num in list: 
      
    # checking condition 
    if num % 2 != 0: 
        out.append(num)
          
  
# printing output
print(out)