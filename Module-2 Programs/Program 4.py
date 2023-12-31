# Write a Python program to check a list is empty or not

# To get input of list from the user
mylist=[]
n=int(input("Enter items in list: "))
for i in range(n):
    x=int(input(f"Enter item {i+1}: "))
    mylist.append(x)
print("List:",mylist)

# To check whether the list is empty or not
if not mylist:
    print("List is empty.")
else:
    print("List is not empty.")