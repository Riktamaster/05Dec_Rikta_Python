# Write a Python function that takes a list of words and returns the length of the longest one

#To get string from the user
mystr=input("Enter list of words: ")

#To split the list of words into single word
words=mystr.split()

#To find the longest word from the string
longest_word=max(words, key=len)

#To find the length of the longest word
length=len(longest_word)

print(f"Length of {longest_word} is {length}")