# Write a Python function to get the largest number, smallest num and sum of all from a list

# To get number of items and items in list
list_number=[]
n=int(input("Enter number of items to form the list: "))
for i in range(n):
    x=int(input(f"Enter number {i+1}: "))
    list_number.append(x)
print("List of numbers:",list_number)

# To get the largest number, smallest number and sum of all numbers in the list
largest_num=max(list_number)
smallest_num=min(list_number)
sum_num=sum(list_number)

# To print the output
print("Largest number:",largest_num)
print("Smallest number:",smallest_num)
print("Sum of all numbers:",sum_num)

