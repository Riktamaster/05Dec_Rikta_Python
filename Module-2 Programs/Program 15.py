# Write a Python program to create a tuple with numbers

# Define data as list
data=[]

# To get input for list from user
n=int(input("Enter number of elements: "))
for i in range(n):
    x=input(f"Enter element {i+1}: ")
    data.append(x)
    
# To print data as tuple
print("Data:",tuple(data))