# Write a Python program to get factorial of a given number

#To get a number from the user
n=int(input("Enter a number:"))

#To find the factorial of the number entered
if n<0:
    print("Factorial is not defined for negative number.")
elif n==0:
    print("Factorial of 0 is 1.")
else:
    fact=1
    for i in range(1,n+1):
        fact *=i
    print(f"The factorial of {n} is {fact}.")
