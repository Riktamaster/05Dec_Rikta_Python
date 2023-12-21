#Write a Python program to swap two numbers using third variable

#To get two numbers from user
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))

#To display numbers before swapping
print("Before swapping")
print("---------------")
print(f"a={a}, b={b}")

#To display number after swapping
temp=a
a=b
b=temp
print("After swapping")
print("--------------")
print(f"a={a}, b={b}")


