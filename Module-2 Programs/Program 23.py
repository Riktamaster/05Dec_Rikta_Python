# Write a Python program to remove an empty tuple(s) from a list of tuples

data=[]
# To get user input for list of tuple
n=int(input("Enter number of tuples:"))
for i in range(n):
    x=input(f"Enter tuple {i+1}:")
    data.append(x)
print("List of tuple before removing empty tuple(s):",data)

# To remove empty tuple(s)
r_tuple=[tup for tup in data if tup]

# To print the revised list of tuples
print("List of tuple after removing empty tuple(s):",r_tuple)
