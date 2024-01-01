# Write a Python program to check whether an element exists within a tuple
# Define data as list
data=[]

# To get input for list from user
n=int(input("Enter number of elements: "))
for i in range(n):
    x=input(f"Enter element {i+1}: ")
    data.append(x)

# To print data in tuple format
print("Data in form of tuple:",tuple(data))

# To get user input of element to check its existence in data
y=input("Enter element to check its existence:")

# To check whether element exists within a tuple or not
if y in data:
    print(f"Element {y} exists within tuple.")
else:
    print(f"Element {y} does not exist within tuple.")