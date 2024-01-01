# Write a Python program to create a tuple with numbers

data=[]

n=int(input("Enter number of elements: "))
for i in range(n):
    x=input(f"Enter element {i+1}: ")
    data.append(x)

print("Data:",tuple(data))