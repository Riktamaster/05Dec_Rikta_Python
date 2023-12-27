# Write a Python function to insert a string in the middle of a string

# To get main string and insert string from user
mystr=input("Enter string: ")
insert_str=input("Enter the string to insert: ")
#To get middle index of main string
middle_index=len(mystr)//2
#To insert a string in the middle of a strin
result=mystr[:middle_index] + ' '+insert_str + mystr[middle_index:]
print("Inserted version of string: ",result)