# Write a function to compute 5/0 and use try/except to catch the exceptions"""  """


try:
    k = 5/0 # raises divide by zero exception.
    print(k)
    
# handles zerodivision exception    
except ZeroDivisionError:   
    print("Can't divide by zero")
        
finally:
    # this block is always executed 
    # regardless of exception generation.
    print('This is always executed') 