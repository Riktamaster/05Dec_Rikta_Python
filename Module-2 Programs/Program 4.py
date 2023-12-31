# Write a Python program to check a list is empty or not
mylist=[]
n=int(input("Enter items in list: "))
for i in range(n):
    x=int(input(f"Enter items{i+1}: "))
    mylist.append(x)
print("List:",mylist)
if not mylist:
    print("List is empty.")
else:
    print("List is not empty.")