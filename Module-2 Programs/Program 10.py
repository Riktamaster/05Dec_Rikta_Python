# Write a Python program to find the second smallest number in a list

# To get input of list from user
mylist=[]
n=int(input("Enter number of items to create list:"))
for i in range (n):
    x=input(f"Enter item {i+1}: ")
    mylist.append(x)
print("List:",mylist)
#To sort the list in ascending order
x=sorted(mylist)
print("Sorted list:",x)

print(f"Second smallest number is {x[1]}")