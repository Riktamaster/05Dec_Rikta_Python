# Write a Python program to convert a list to a tuple

# Define data as list
data=[]

# To get input for list from user
n=int(input("Enter number of elements: "))
for i in range(n):
    x=input(f"Enter element {i+1}: ")
    data.append(x)

# To convert list to a tuple and print it
print("Data in form of tuple:",tuple(data))