""" 10. Generate and print another tuple whose values are even numbers in the given tuple
(1,2,3,4,5,6,7,8,9,10). """

tp=(1,2,3,4,5,6,7,8,9,10)
even=list()
for i in tp:
    if i%2==0:
        even.append(i)
print("List is:" ,even)        
tpeven=tuple(even)
print(tpeven)
    
      
    