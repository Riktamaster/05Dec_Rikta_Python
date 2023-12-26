# Write a Python program to count the occurrences of each word in a given sentence

#To get string from the user
mystr=input("Enter string:")

#To split the string into words
words=mystr.split()

#To count occurences of each word in given string
for i in words:
    frequency=words.count(i)
    print(f"{i}:{frequency}")