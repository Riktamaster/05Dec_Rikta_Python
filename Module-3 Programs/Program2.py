# Write a Python program to append text to a file and display the text

# To open the text file
f=open('demo.txt','a')

# To add new text to the file
new_text="This is new text that has been appended!\n"
f.write(new_text)

# To read the entire contents of the file
file_content=f.read()

# To print the contents of the file
print("Updated file content:",file_content)