# Write a Python program to split a list into different variables

# Define a list
data=[]
# To get user input for list
n=int(input("Enter number of items in list:"))
for i in range(n):
    x=input(f"Enter item {i+1}:")
    data.append(x)

# To unpack the list into different variables dynamically   
*variables,=data

# To print the variables
print("--------------")
for i, value in enumerate(variables, start=1):
    print(f"var{i}:", value)