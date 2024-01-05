# Write a Python function that checks whether a passed string is palindrome or not

# To create a function for checking if a string is palindrome or not
def string_pal(mystr):
    #Reverse the string using slicing
    rev_str=mystr[::-1]
    #Check if the original and reversed string are same
    if mystr==rev_str:
        print("It is a palindrome.")
    else:
        print("It is not palindrome.")

# To get user input for string
mystr=str(input("Your string:"))
string_pal(mystr) # Call the user define function