# Write a Python function to check whether a number is perfect or not

# To create user defined function to check whether a number is perfect or not
def check_perfect(n):
    sum=0 # varaible to store sum of divisors
    for i in range(1,n): # iterate through numbers from 1 to n-1 
        if(n%i==0): # to check if i is a divisor of n
            sum+=i # add i to the sum_of_divisors if it is a divisor
    # Check if the sum of divisors equals the original number
    if (sum==n):
        print(f"{n} is a perfect number.")
    else:
        print(f"{n} is not a perfect number.")

# Get user input for the number to check
n=int(input("Enter your number: "))

# Call the function with the user-provided value
check_perfect(n)