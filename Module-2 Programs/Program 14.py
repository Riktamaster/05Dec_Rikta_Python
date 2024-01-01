# Write a Python program to create a tuple with different data types

# Define data as list
data=[]

# To get input for an integer data type from user
int_value=int(input("Enter element integer type: "))
data.append(int_value)

# To get input for float data type from user
float_value=float(input("Enter element float type: "))
data.append(float_value)

# To get input for string data type from user
str_value=str(input("Enter element string type: "))
data.append(str_value)

# To get input for boolean data type from user
boolean_value=bool(input("Enter element boolean type: "))
data.append(boolean_value)

# To print the resulting tuple(converting list into tuple)
print("Tuple with different data types:",tuple(data))