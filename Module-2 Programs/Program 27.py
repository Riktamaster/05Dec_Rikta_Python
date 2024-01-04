# Write a Python script to concatenate following dictionaries to create a new one

# To get user input for dictionary 1
dict1={}
n=int(input("Enter number of pairs for dictionary 1:"))
for i in range(n):
    k1=input("Enter keys for dictionary 1:")
    v1=input("Enter values for dictionary 1:")
    dict1[k1]=v1

# To get user input for dictionary 2
dict2={}
m=int(input("Enter number of pairs for dictionary 2:"))
for j in range(m):
    k2=input("Enter keys for dictionary 2:")
    v2=input("Enter values for dictionary 2:")
    dict2[k2]=v2
print("---------------------------------------")
print("Dictionary 1:",dict1)
print("Dictionary 2:",dict2)

# To concatenate dictionary 1 and dictionary 2 to create dictionary 3
dict3={**dict1,**dict2}
print("Dictionary 3(Concatenated dictionary):",dict3)