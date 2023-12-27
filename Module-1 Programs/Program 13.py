# Write a Python program to count occurrences of a substring in a string

#To get input for string and substring from user
mystr=input("Enter string: ")
substr=input("Enter substring from the string entered: ")

#To count the occurences of substring
count=mystr.count(substr)

#To print the count of occurences of substring
print(f"{substr} appears {count} times in my string.")