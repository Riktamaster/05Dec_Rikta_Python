# Write a Python script to sort (ascending and descending) a dictionary by value

# Define an empty dictionary
mydict={}

# To get user input for dictionary
n=int(input("Enter number of paris to create dictionary:"))
for i in range(n):
    k=input("Enter keys:")
    v=input("Enter values:")
    mydict[k]=v
print("Original dictionary:",mydict)

# To sort and print the dictionary in ascending order
asc=dict(sorted(mydict.items()))
print("Ascending order of dictionary:",asc)

# To sort and print the dictionary in descending order
dsc=dict(sorted(mydict.items(),reverse=True))
print("Descending order of dictionary:",dsc)