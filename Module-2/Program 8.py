# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

#To get two numbers from user
num1=float(input("Enter value for number 1: "))
num2=float(input("Enter value for number 2: "))
num3=float(input("Enter value for number 3: "))

#To get summation of given three integers
if num1==num2 or num2==num3 or num3==num1:
    print("The sum of given three integers is 0.") 
else:
    n=num1+num2+num3
    print(f"The sum of given three integers is {n}.")