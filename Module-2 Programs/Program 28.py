# Write a Python script to check if a given key already exists in a dictionary

# Define an empty dictionary
mydict={}

# To get user input for dictionary
n=int(input("Enter number of pairs to create dictionary:"))
for i in range(n):
    k=input("Enter keys:")
    v=input("Enter values:")
    mydict[k]=v
print("Original dictionary:",mydict)

# To check whether the given key already exists or not
check_key=input("Enter key to check:")
if check_key in mydict:
    print("Yes")
else:
    print("No")