""" Define a class named Shape and its subclass Square. The Square class has an init function which
takes length as argument. Both classes have an area function which can print the area of the shape
where Shape’s area is 0 by default. """

class shape:

    def __init__(self, sidelen):
        self.sidelen = sidelen
    def area(self):
        print("The area is 0")

class square(shape):

    def area(self):
        totalarea= self.sidelen*2
        print("The total area is: ",totalarea)

s=square(20)
s.area()