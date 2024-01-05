'''Write a Python program to create and display all combinations of letters, 
selecting each letter from a different key in a dictionary.
Sample data: {'1': ['a','b'], '2': ['c','d']}
Expected Output: ac ad bc bd'''

import itertools
mydict={}
# To get user input for dictionary
n=int(input("Enter number of pairs to create dictionary:"))
for i in range(n):
    k=input("Enter keys:")
    v=input("Enter values:")
    mydict[k]=v.split(',')
print("Original dictionary:",mydict)

# Generate and display combinations
print("------------------")
print("Output:")
for combination in itertools.product(*mydict.values()):
    
    print(''.join(combination))