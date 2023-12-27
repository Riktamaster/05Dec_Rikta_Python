# Write a Python function to reverses a string if its length is a multiple of 4

#To get string from the user
mystr=input("Enter string: ")

#To reverse the entered string using string slicing
rev_mystr=''.join(reversed(mystr))

#To print the reversed string if its length is a multiple of 4
if len(rev_mystr)%4==0:
    print(rev_mystr)
else:
    print(mystr)