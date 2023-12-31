# Write a Python function that takes a list and returns a new list with unique elements of the first list

# To get input of list from user
list=[]
n=int(input("Enter number of items for list:"))
for i in range(n):
    x=input(f"Enter list item {i+1}: ")
    list.append(x)
print("Original list:",list)

# To get a new list with unique items of first list
new_list=[]
for item in list:
    if item not in new_list:
        new_list.append(item)

# To print unique items from first list
print("New list with unique items:", new_list)
