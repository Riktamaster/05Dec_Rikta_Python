# Write a Python program to returns sum of all divisors of a number

# To create user defined function to return sum of all divisors of a number
def sum_of_divisors(n):
    sum=0 # varaible to store sum of divisors
    for i in range(1,n): # iterate through numbers from 1 to n-1 
        if(n%i==0): # to check if i is a divisor of n
            sum+=i # add i to the sum_of_divisors if it is a divisor
    return sum

# To get user input for number
n=int(input("Enter number:"))

# To print the result
print(f"Sum of all divisors of {n} is:",sum_of_divisors(n))