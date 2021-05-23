""" Write a program to construct a dictionary from the two lists containing the names of students and
their corresponding subjects. The dictionary should map the students with their respective subjects.
Let’s see how to do this using for loops and dictionary comprehension.
HINT - Use Zip function also
Sample input: students = ['Smit', 'Jaya', 'Rayyan'] subjects = ['CSE', 'Networking', 'Operating System']
Expected output: {‘Smit’ : ’CSE’ , ’Jaya’ : ’Networking’ , ’Rayyan’ : ’Operating System’} """

 #initializing lists
students = ["Smit", "Jaya", "Rayyan"]
subjects = ["CSE","Networking","Operating Sysytem"]

res = {}
for key in students:
    for value in subjects:
        res[key] = value
       
# Printing resultant dictionary 
print ("Resultant dictionary is : " +  str(res))



# using dictionary comprehension
# to convert lists to dictionary
#print(len(students))
res = {students[i]: subjects[i] for i in range(len(students))}
  
# Printing resultant dictionary 
print ("Resultant dictionary is : " , str(res))