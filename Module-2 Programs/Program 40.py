# Write a Python function to check whether a number is in a given range

# User define function to check whether a number is in a given range or not
def num_range (n,x,y):
    if x<=n<=y:
        print(f"Number {n} is in the given range.")
    else:
        print(f"Number {n} is not in the given range.")
        
# To get user input for lower limit of the range to be defined
x=int(input("Enter lower limit of the range:"))

# To get user input for upper limit of the range to be defined
y=int(input("Enter upper limit of the range:"))

# To get user input for the number to be checked
n=int(input("Enter the number:"))

# calling the user defined function
num_range(n,x,y)