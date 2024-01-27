'''Write a Python class named Rectangle constructed by a length and width 
and a method which will compute the area of a rectangle'''

# To create a class named rectangle
class Rectangle:
    # To get user input for length of rectangle
    l=float(input("Enter value for length of a rectangle:"))
    # To get user input for width of a rectangle
    w=float(input("Enter value for width of a rectangle:"))
    # To create UDF for calculating area of rectangle
    def compute(self):
        print("Area of rectangle is:", self.l*self.w)
        
# To create object for class rectangle
Area=Rectangle()
# To call UDF to compute the area
Area.compute()