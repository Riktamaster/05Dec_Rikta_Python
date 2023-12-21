# Write a Python program to test whether a passed letter is a vowel or not

#To get the alphabet from user
alphabet=(input("Enter a single alphabet:"))

#To find out whether the passes letter is vowel or not
if alphabet in ['A','a','E','e','I','i','O','o','U','u']:
    print(f"{alphabet} is a vowel.")
else:
    print(f"{alphabet} is a consonant.")

