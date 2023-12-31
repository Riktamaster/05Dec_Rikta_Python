# Write a Python program to convert a list of characters into a string

# To get input of list from user
list=[]
n=int(input("Enter number of items to create list:"))
for i in range(n):
    x=input(f"Enter character {i+1}:")
    list.append(x)
print("List of characters:",list)

# To convert list of characters into string
str=''.join(list)
print(f"String is {str}")