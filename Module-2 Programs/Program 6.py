''' Write a Python program to generate and print a list of first and last 5 elements 
where the values are square of numbers between 1 and 30'''
#To define a list
list=[]

#To generate list of square of first and last 5 numbers between 1-30
for i in range(1,31):
    list.append(i*i)

#To print the result
print(f"Square of first 5 numbers between 1 and 30:{list[:5]}")
print(f"Square of last 5 numbers between 1 and 30:{list[-5:]}")