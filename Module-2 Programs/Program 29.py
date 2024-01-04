# Write a Python script to print a dictionary where the keys are numbers between 1 and 15
# Define an empty dictionary
mydict={}

# To get user input for dictionary
n=int(input("Enter number of pairs to create dictionary:"))
for i in range(n):
    k=int(input("Enter keys (numbers between 1 and 15):"))
    if k>=1 and k<=15: # To allow only keys with numbers between 1 and 15 to be entered
        v=input("Enter values:")
        mydict[k]=v
    else:
      print("Invalid number entered! Please enter numbers between 1 and 15.")
print("Original dictionary:",mydict)