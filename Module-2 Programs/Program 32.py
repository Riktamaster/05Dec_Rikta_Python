# Write a Python program to map two lists into a dictionary

# To get user input for list of keys
keys_list=(input("Enter list of keys(separated by space):")).split()

# To get user input for list of values
values_list=(input("Enter list of values(separated by space):")).split()

# To map lists of keys and values into a dictionary
mapped_dict=dict(zip(keys_list,values_list))

# To print the mapped dictionary
print("Mapped dictionary:",mapped_dict)