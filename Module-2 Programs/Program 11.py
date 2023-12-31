# Write a Python program to get unique values from a list

# To get input of list from user
mylist=[]
n=int(input("Enter number of items to create list:"))
for i in range (n):
    x=input(f"Enter item {i+1}: ")
    mylist.append(x)

# To get unique values using set
new_list=list(set(mylist))

# To print the result
print("Original list:",mylist)
print("Unique values:",new_list)