# Write a Python program to find the repeated items of a tuple
# Define data as list
data=[]

# To get input for list from user
n=int(input("Enter number of elements: "))
for i in range(n):
    x=input(f"Enter element {i+1}: ")
    data.append(x)
    if data.count(x)>1:
        data.append(x)
print(tuple(data))

#Find and print repeated items
repeated_items = set(item for item in data if data.count(item) > 1)
print("Repeated items:", repeated_items)