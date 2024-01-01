# Write a Python program to create a tuple with different data types

data=[]

int_value=int(input("Enter element integer type: "))
data.append(int_value)

float_value=float(input("Enter element float type: "))
data.append(float_value)

str_value=str(input("Enter element string type: "))
data.append(str_value)

boolean_value=bool(input("Enter element boolean type: "))
data.append(boolean_value)

print("Tuple with different data types:",tuple(data))