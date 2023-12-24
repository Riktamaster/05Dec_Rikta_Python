# Write a python program to sum of the first n positive integers

# To get the value of n from user
n = int(input("Enter a positive integer (n): "))

# To perform summation of (n) value entered by user
if n <= 0:
    print("Enter a positive integer.")
else:
    sum = (n * (n + 1))/2
    print(f"The sum of the first {n} positive integers is: {sum}")

