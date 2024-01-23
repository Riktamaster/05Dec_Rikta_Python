# Write a Python program to read last n lines of a file

# To open the text file
f=open('demo.txt', 'r')

# Get user input for the number of lines to read
n = int(input("Enter number of lines to read:"))

# Read and print the last n lines using negative index
print(f"Last {n} lines:")
for i, line in enumerate(f.readlines()[-n:], start=1):
        print(f"Line [{i}]: {line.strip()}")
