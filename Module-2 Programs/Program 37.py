'''Write a Python program to combine values in python list of dictionaries. 
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':300}, 
{'item': 'item1', 'amount': 750}]
Expected Output:
Counter ({'item1': 1150, 'item2': 300})'''

from collections import Counter

# Get user input for the list of dictionaries
data = []
n = int(input("Enter the number of dictionaries in the list: "))
for i in range(n):
    item = input("Enter item: ")
    amount = int(input("Enter amount: "))
    data.append({'item': item, 'amount': amount})

# To combine all values in dictionary
com_values=Counter()
for i in data:
    item=i['item']
    amount=i['amount']
    com_values[item]+=amount
    
# To print the result
print(com_values)

