'''Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, 
if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. 
Return the resulting string.'''

#To get string from user
mystr=input("Enter string: ")

#To carry out the required modifications in entered string
not_str=mystr.find('not')
poor_str=mystr.find('poor')

if poor_str>not_str and poor_str>0 and not_str>0:
    new_str=mystr.replace(mystr[not_str:(poor_str+4)], 'good')
    print(new_str)
else:
    print(mystr)