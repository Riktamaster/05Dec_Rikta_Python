'''Write python program that user to enter only odd numbers, 
else will raise an exception.'''


try:
    n = int(input("Enter an odd number: "))
    if n % 2 != 0:
        print(f"You entered a valid odd number: {n}")
    else:
        raise ValueError
except:
    print("Error: Please enter an odd number.")
