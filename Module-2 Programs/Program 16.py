# Write a Python program to convert a tuple to a string

# Define data as list
data=[]

# To get input for list from user
n=int(input("Enter number of elements: "))
for i in range(n):
    x=input(f"Enter element {i+1}: ")
    data.append(x)

# To convert list into tuple
y=tuple(data)

# To convert tuple into string
str=''.join(data)
print("Data in string form:",str) 

