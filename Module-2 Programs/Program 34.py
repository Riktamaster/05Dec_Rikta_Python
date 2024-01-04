# Write a Python program to print all unique values in a dictionary

# Define an empty dictionary
mydict={}

# To get user input for dictionary
n=int(input("Enter number of pairs to create dictionary:"))
for i in range(n):
    k=(input("Enter keys:"))
    v=input("Enter values:")
    mydict[k]=v
print("Original dictionary:",mydict)

# Set to store unique values
unique_values=set()

# To traverse through the dictionary
for value in mydict.values():
    unique_values.add(value)
    
# Print the unique values
print("Unique values:",unique_values)