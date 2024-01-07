# Write a Python program to calculate surface area and volume of a cylinder

# To create an anonymous function to calculate surface volume and area of a cylinder
surface_area=lambda h,r:((2*3.14*r)*h)+((3.14*r**2)*2)
volume=lambda h,r:3.14*r*r*h

# To get user input for heigth and radius of a cylinder
h=float(input("Enter value for height: "))
r=float(input("Enter value for radius: "))

# To print the result
print("--------------------------------")
print("Surface area of cylinder is:",surface_area(h,r))
print("Volume of cylinder is:",volume(h,r))