# Write a Python program to find the maximum and minimum numbers from the specified decimal numbers

# To create UDF to find maximum and minimum numbers from list of decimal numbers
def min_max(numbers):
    max_num=max(numbers)
    min_num=min(numbers)

    return max_num, min_num

# Define an empty list to store decimal values
number=[]

# To add user input values to the list
n=int(input("Enter number of values to add to the list: "))
for i in range(n):
    x=float(input(f"Enter number {i+1}: "))
    number.append(x)

# To call the UDF
max_value, min_value = min_max(number)

# To print the result
print("---------------------------------")
print("List of decimal numbers:",number)
print(f"Maximum number: {max_value}")
print(f"Minimum number: {min_value}")