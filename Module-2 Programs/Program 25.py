# Write a Python program to convert a list of tuples into a dictionary

# Define a tuple
data=[]

# To get user input for list of tuple
n=int(input("Enter number of tuples: "))
for i in range(n):
    x=input(f"Enter tuple list {i+1} (comma separated values):")
    values = tuple(x.split(','))
    data.append(values)

# To convert list of tuple into dictionary and print the result
print("List of tuples:",data)
print("Resulting dictionary:",dict(data))