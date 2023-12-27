'''Write a Python program to find whether a given number is even or odd, 
print out an appropriate message to the user.'''
#To get a positive number from user
n=int(input("Enter a number:"))

#To find out whether the number is even or odd

if n%2==0:
    print(f"{n} is an even number.")
else:
    print(f"{n} is an odd number.")

