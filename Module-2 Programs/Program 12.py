# Write a Python program to check whether a list contains a sub list
# To get input for two lists from the user
main_list=[]
sub_list=[]
n=int(input("Enter number of items for main list:"))
m=int(input("Enter number of items for sub list:"))
for i in range(n):
    x=input("Enter items for main list:")
    main_list.append(x)
for j in range(m):
    y=input("Enter items for sub list:")
    sub_list.append(y)

if all(item in main_list for item in sub_list):
    print("Main list contains sub list.")
else:
    print("Main list does not contains sub list.")