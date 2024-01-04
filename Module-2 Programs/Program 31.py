# Write a Python script to merge two Python dictionaries
# To get user input for dictionary 1
dict1={}
n=int(input("Enter number of pairs for dictionary 1:"))
for i in range(n):
    k1=input(f"Enter key {i+1}:")
    v1=input(f"Enter value {i+1}:")
    dict1[k1]=v1

# To get user input for dictionary 2
dict2={}
m=int(input("Enter number of pairs for dictionary 2:"))
for j in range(m):
    k2=input(f"Enter key {j+1}:")
    v2=input(f"Enter value {j+1}:")
    dict2[k2]=v2
print("---------------------------------------")
print("Dictionary 1:",dict1)
print("Dictionary 2:",dict2)

# To merge dictionary 1 and dictionary 2
dict1.update(dict2)
print("Merged Dictionary:",dict1)