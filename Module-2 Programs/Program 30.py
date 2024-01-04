# Write a Python program to check multiple keys exists in a dictionary

# Define an empty dictionary
mydict={}

# To get user input for dictionary
n=int(input("Enter number of pairs to create dictionary:"))
for i in range(n):
    k=(input("Enter keys:"))
    v=input("Enter values:")
    mydict[k]=v
print("Original dictionary:",mydict)

# To get user input for multiple keys
check_keys=input("Enter multiple keys (space separated):").split()
for key in check_keys:
    if key in mydict:
        print(f"Key {key} exists in the dictionary with value:{mydict[key]}")
    else:
        print(f"Key {key} does not exist in the dictionary.")