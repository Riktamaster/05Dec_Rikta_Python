# Write a Python program to read a file line by line and store it into a list

# To open the text file
f=open('demo.txt', 'r')

lines=f.readlines()

# Print the contents of the file line by line and store it into a list
if lines:
    print(f"Contents of {'demo.txt'}:")
    for line in lines:
        print(line.strip())  # Strip newline characters for cleaner output