# Write a Python program to replace last value of tuples in a list

# Define data as list
data=[]

# To get input for list from user
n=int(input("Enter number of elements: "))
for i in range(n):
    x=input(f"Enter element {i+1}: ")
    data.append(x)
print("Data in form of list:", data)

# To replace last value in list
y=input("Enter value to replace the last element:")
data[-1]=y

# To print the result in tuple format
print("Data in form of tuple:",tuple(data))