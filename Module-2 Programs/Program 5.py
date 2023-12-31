# Write a Python function that takes two lists and returns true if they have at least one common member

# To get input for two lists from the user
list1=[]
list2=[]
n=int(input("Enter number of items for list 1:"))
m=int(input("Enter number of items for list 2:"))
for i in range(n):
    x=input("Enter elements in list-1:")
    list1.append(x)
for j in range(m):
    y=input("Enter intems for list-2:")
    list2.append(y)
print("List-1:",list1)
print("List-2:",list2)
for item in list1:
    if item in list2:
        print("True")
        break
else:
    print("False")