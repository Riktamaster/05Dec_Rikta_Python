# Write a Python program to write a list to a file

# To get input of list from user
mylist=[]
n=int(input("Enter number of items to create list:"))
for i in range (n):
    x=input(f"Enter item {i+1}: ")
    mylist.append(x)
    
# To write the entered list into a file
f=open('demo.txt','w')
for item in mylist:
    f.write(f"{item}\n")

print(f"The list has been successfully written to {'demo.txt'}")