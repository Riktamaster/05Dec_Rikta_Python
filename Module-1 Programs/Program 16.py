''' Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing' then add 'ly' 
instead if the string length of the given string is less than 3, leave it unchanged.'''

#To get string from the user
mystr=input("Enter string: ")

#To carry out required modifications in entered string
if len(mystr)<3:
    print(mystr)
elif mystr.endswith('ing'):
    new_str=mystr+"ly"
    print(new_str)
else:
    new_str=mystr+'ing'
    print(new_str)
