# Write a Python program to find the highest 3 values in a dictionary
# Define an empty dictionary
mydict={}

# To get user input for dictionary
n=int(input("Enter number of pairs to create dictionary:"))
for i in range(n):
    k=(input("Enter keys:"))
    v=input("Enter values:")
    mydict[k]=v
print("Original dictionary:",mydict)

# To sort the dictionary in descending order
dsc=dict(sorted(mydict.items(), reverse=True))

# To print and get the highest three values from the sorted dictionary
print("Highest three values:")
for value in list(dsc.values())[:3]:
    print(f"{value}")