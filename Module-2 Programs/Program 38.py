'''Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string: 'w3resource'
Expected output:
{'3': 1,'s': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}'''

# To get user input for string
mystr=str(input("Enter your string:"))
print("-----------------------------")
print("Your string:",mystr)

# To define an empty dictionary
mydict={}

# To count the characters in string and store in dictionary
for i in mystr:
    mydict[i]=mystr.count(i)

# To print the resultant dictionary
print("Output:",mydict)