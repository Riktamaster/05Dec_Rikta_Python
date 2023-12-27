#Write a Python program to swap two numbers without using third variable

#To get two numbers from user
a=float(input("Enter value of a:"))
b=float(input("Enter value of b:"))

#To display two numbers before swapping
print("Before swapping")
print("---------------")
print(f"a={a}, b={b}")

#To display two numbers after swapping
a,b=b,a
print("After swapping")
print("--------------")
print(f"a={a}, b={b}")