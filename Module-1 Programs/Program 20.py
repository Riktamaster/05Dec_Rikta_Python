'''Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
If the string length is less than 2, return instead of the empty string.'''
#To get string from the user
mystr=input("Enter string: ")

#To apply the given conditions
if len(mystr)<2:
    print("Empty string")
else:
    new_str=mystr[:2] + mystr[-2:]

print(new_str)