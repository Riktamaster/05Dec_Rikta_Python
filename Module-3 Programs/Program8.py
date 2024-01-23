# Write a Python program to count the number of lines in a text file

# To open the text file
f = open('demo.txt', 'r')

# Read the entire content of the file and count the newline characters
line_count=f.read().count('\n')

# To print the result
print(f"Number of lines in {'demo.txt'}: {line_count}")