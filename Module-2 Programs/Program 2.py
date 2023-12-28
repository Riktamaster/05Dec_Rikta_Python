'''Write a Python program to count the number of strings where the string length is 2 or more 
and the first and last character are same from a given list of strings'''

# To get number of strings to add to the list
list_string=[]
str=int(input("Enter number of items for the list: "))
for i in range(str):
    x=input(f"Enter string {i+1}: ")
    list_string.append(x)

# To print the list
print("List:",list_string)

# To count the number of strings where the first and last character are same
count=0
for s in list_string:
    if len(s)>=2 and s[0]==s[-1]:
        count+=1

# To print the result
print(f"Number of strings with the same first and last character: {count}")