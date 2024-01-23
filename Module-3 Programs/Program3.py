# Write a Python program to read first n lines of a file

# To open the text file
f=open('demo.txt','r')

# To get user input for number of lines to read
n=int(input("Enter number of lines to read:"))

# To read first n lines of a file
for i in range(n):
    line=f.readline()
    print(f"Line:[{i+1}] = {line}")
