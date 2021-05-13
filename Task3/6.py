""" 6. Create a list of elements such that it contains the squares of the first and last 5 elements between
1 and30 (both included). """

def printValues():
	l = list()
	for i in range(1,31):
		l.append(i**2)
	print(l[:5])
	print(l[-5:])

printValues()