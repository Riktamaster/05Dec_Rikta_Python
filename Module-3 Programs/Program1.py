#Write a Python program to read an entire text file
# open('demo.txt','w') ---> To create a text file

# To open the text file in read mode
f=open('demo.txt','r')

# To read the entire contents of the file
file_content=f.read()

# To print the contents of the file
print("File content:",file_content)