""" Write a program in python to print the pair of numbers whose sum is equal to the result
number that is let's say 8.
x=[1,2,3,4,5,6,7,8,9,-1] """

def printPairs(x, n, sum):
 
    # count = 0
 
    # Consider all possible
    # pairs and check their sums
    for i in range(0, n ):
        
        for j in range(i + 1, n ):
            #print("x[i] is :", x[i])
            #print("x[j] is :", x[j])
            if (x[i] + x[j] == sum):
               print("(", x[i],
                      ", ", x[j],
                      ")", sep = "")
  
 
# Driver Code
x=[1,2,3,4,5,6,7,8,9,-1]
n = len(x)
print(n)
sum = 8
printPairs(x, n, sum)
 