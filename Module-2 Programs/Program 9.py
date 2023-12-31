# Write a Python program to select an item randomly from a list
import random
# To get input of list from user
mylist=[]
n=int(input("Enter number of items to create list:"))
for i in range (n):
    x=input(f"Enter item {i+1}: ")
    mylist.append(x)
print("List:",mylist)

# To select random item from the list
print("Randon item: ",random.choice(mylist))