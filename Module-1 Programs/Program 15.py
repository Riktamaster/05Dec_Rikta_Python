'''Write a Python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string.'''

# To get two strings from user
mystr1=input("Enter string 1: ")
mystr2=input("Enter string 2: ")

# To swap first two characters of each string
nmystr1=mystr1[1] + mystr1[0] + mystr1[2:] 
nmystr2=mystr2[1] + mystr2[0] + mystr2[2:]

#To get single string after modification
new_str=nmystr1 + ',' + nmystr2
print("New string: ",new_str)