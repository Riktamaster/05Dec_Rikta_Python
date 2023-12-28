# Write a Python program to remove duplicates from a list

list=[]
n=int(input("Enter number of items to form the list: "))
for i in range(n):
    x=input(f"Enter items {i+1}: ")
    list.append(x)

# To remove duplicate items from the list
new_list=[]
for i in list:
    if i not in new_list:
        new_list.append(i)

# To print the result
print("Original list:",list)
print("List after removing duplicates:",new_list)