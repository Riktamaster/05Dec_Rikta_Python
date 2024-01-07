# Write a Python program to calculate the area of a parallelogram

# To create an anonymous function to calculate area of a parallelogram
area=lambda b,h:b*h

# To get user input for base and height of a parallelogram
b=float(input("Enter value for base: "))
h=float(input("Enter value for height: "))

# To print the result
print("-------------------------------")
print("The area of parallelogram is: ",area(b,h))