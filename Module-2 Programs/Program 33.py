'''Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,'d':400}
Sample output: Counter ({'a': 400, 'b': 400,'d': 400, 'c': 300})'''

from collections import Counter
# To get user input for dictionary 1
dict1={}
n=int(input("Enter number of pairs for dictionary 1:"))
for i in range(n):
    k1=input(f"Enter key {i+1}:")
    v1=int(input(f"Enter value {i+1}:"))
    dict1[k1]=v1

# To get user input for dictionary 2
dict2={}
m=int(input("Enter number of pairs for dictionary 2:"))
for j in range(m):
    k2=input(f"Enter key {j+1}:")
    v2=int(input(f"Enter value {j+1}:"))
    dict2[k2]=v2
print("---------------------------------------")
print("Dictionary 1:",dict1)
print("Dictionary 2:",dict2)

# Create counters from dictionaries
c1=Counter(dict1)
c2=Counter(dict2)

# Convert result to a dictionary
result=c1+c2
result_dict=dict(result)

# To print the result
print("Resultant dictionary:",result_dict)