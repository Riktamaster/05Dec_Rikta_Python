# Write a Python program to copy the contents of a file to another file

# To create and open source file
f=open('demo.txt','r')

# To create and open where the contents of source file needs to be copied
d=open('destination.txt','w')

# Read the contents of the source file-->demo.txt
content = f.read()

# Write the contents to the destination file
d.write(content)

print(f"Contents of {'demo.txt'} copied to {'destination.txt'}.")