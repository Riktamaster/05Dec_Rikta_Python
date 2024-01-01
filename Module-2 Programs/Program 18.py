# Write a Python program to find the length of a tuple
# Define data as list
data=[]

# To get input for list from user
n=int(input("Enter number of elements: "))
for i in range(n):
    x=input(f"Enter element {i+1}: ")
    data.append(x)

# To print data in tuple format
print("Data in form of tuple:",tuple(data))

# To calculate length of tuple
y=len(data)
print("Length of tuple:",y)