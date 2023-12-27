# Write a Python program to count the number of characters (character frequency) in a string

#To get input of a string from user
mystr=input("Enter string: ")

#To count the number of characters (character frequency) in a string
for i in mystr:
    frequency=mystr.count(i)
#To print the characters in a string
    print(f"{i}: {frequency}")