'''Write a Python program that will return true if the two given integer values are equal 
or their sum or difference is 5.'''

#To get two integers from user
a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))

#To return true if given two integers are equal or their sum or difference is 5
if a==b or a+b==5 or a-b==5:
    print("True")
else:
    print("False")