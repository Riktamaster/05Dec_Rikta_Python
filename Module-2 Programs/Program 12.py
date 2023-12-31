# Write a Python program to check whether a list contains a sub list

# To get input of main list from the user
main_list=[]
n=int(input("Enter number of items for main list:"))
for i in range(n):
    x=input(f"Enter item {i+1}:")
    main_list.append(x)

# To get input of sub list from the user
sub_list=[]
m=int(input("Enter number of items for sub list:"))
for j in range(m):
    y=input(f"Enter item {i+1}:")
    sub_list.append(y)

# To check whether main list contains sub list
if all(item in main_list for item in sub_list):
    print("Main list contains sub list.")
else:
    print("Main list does not contains sub list.")