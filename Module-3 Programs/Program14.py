'''Write a Python class named Circle constructed by a radius 
and two methods which will compute the area and the perimeter of a circle'''

# To create a class named Circle
class Circle:
    # To get user input for radius of circle
    r=float(input("Enter value for radius of a circle:"))
    
    # To create UDF for calculating area of circle
    def compute_area(self):
        print("Area of circle is:", 3.14*self.r*self.r)

    # To create UDF for calculating perimeter of circle
    def compute_perimeter(self):
        print("Area of circle is:", 2*3.14*self.r)
        
# To create object for class Circle
circle=Circle()
# To call UDF to compute the area
circle.compute_area()
# To call UDF to compute the perimeter
circle.compute_perimeter()