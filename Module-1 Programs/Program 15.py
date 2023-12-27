# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string

# To get two strings from the user
str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")

# To swap the first two characters using replace
new_str1 = str2[0:2] + str1[2:]
new_str2 = str1[0:2] + str2[2:]

# To get a single string separated by a space
mystr = new_str1 + " " + new_str2

# To print the result
print(f"New string: {mystr}")
