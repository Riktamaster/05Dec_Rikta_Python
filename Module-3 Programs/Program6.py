# Write a Python program to read a file line by line store it into a variable

# To open the text file
f=open('demo.txt', 'r')

# To read lines and concatenate them into variable
file_content=''.join(f.readlines())
print(f"Contents of {'demo.txt'}:\n",file_content)