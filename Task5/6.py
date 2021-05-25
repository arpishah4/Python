""" Read doc.txt file using Python File handling concept and return only the even length string from
the file. Consider the content of doc.txt as given below:
Hello I am a file
Where you need to return the data string
Which is of even length
Make sure you return the content in The same link as it is present. """


file1 = open('file.txt', 'w')
L = ["Hello I am a file \n", "Where you need to return the data string \n", "which is even length \n"]
file1.writelines(L)
file1 = open("file.txt", "a")  # append mode
file1.write("ArpiShah")

file1 = open('file.txt', 'r')
#print(file1.read())
len(file1.readlines())
for line in file1.readlines():
    print(line)
print(file1.read())
#file1.close()

"""f = open("file6.txt", "r")
#print(f.readlines())
read=f.readlines()
print(read)
for i in read:
    if len(i)%2==0:
        print(i)
"""
