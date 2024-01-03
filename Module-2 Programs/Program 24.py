# Write a Python program to unzip a list of tuples into individual lists

data=[]

# To get user input for list of tuple
n=int(input("Enter number of tuples:"))
for i in range(n):
    x=input(f"Enter tuple {i+1} (comma separated values):")
    values = tuple(x.split(','))
    data.append(values)
print("Zipped list of tuple:",data)

# To unzip a list of tuples into individual lists
unzip_data=list(zip(*data))
print("Unzipped list of tuples:",unzip_data)