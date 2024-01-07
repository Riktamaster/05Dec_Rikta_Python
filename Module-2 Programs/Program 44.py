# Write a Python program to convert degree to radian

# To create anonymous function for conversion of degree to radian
radian=lambda x:x*(3.14/180) 

# To get user input for the degree of angle
x=float(input("Enter degrees:"))

# To print the result
print(f"The conversion of {x} degree(s) is {radian(x)} radian.")