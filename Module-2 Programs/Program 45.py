# Write a Python program to calculate the area of a trapezoid

# To create an anonymous function to calculate area of a trapezoid
area=lambda b1,b2,h:((b1+b2)/2)*h

# To get user input for base1, base2 and height of a trapezoid
b1=float(input("Enter value for base 1: "))
b2=float(input("Enter value for base 2: "))
h=float(input("Enter value for height: "))

# To print the result
print("---------------------------")
print("Area of trapezoid =",area(b1,b2,h))