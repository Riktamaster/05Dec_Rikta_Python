# Write a Python function to calculate the factorial of a number (a nonnegative integer)

#Function to calculate factorial of a number
def cal_fact():
    fact=1
    for i in range(1,n+1):
        fact *=i
    print(f"The factorial of {n} is {fact}.")

# To get user input of the number to calculate its factorial
n=int(input("Enter a positive integer:"))

# To call the calculation function
cal_fact()