
# Create a class to find three elements that sum to zero from a set of n real numbers

def findTriplets(arr, n):
 
    found = False
    list1=[]
    for i in range(0, n-2):
        for j in range(i+1, n-1):
           
            for k in range(j+1, n):
             
                if (arr[i] + arr[j] + arr[k] == 0):
                    a=arr[i], arr[j], arr[k]
                    print([a])
                    #list1.append=a
                    #print(list1)
                    found = True
   
             
    # If no triplet with 0 sum
    # found in array
    if (found == False):
        print(" not exist ")
 
# Driver code
arr = [0, -1, 2, -3, 1]
n = len(arr)
print("LENGTH IS :",n)
findTriplets(arr, n)