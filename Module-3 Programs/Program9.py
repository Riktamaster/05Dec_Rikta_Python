# Write a Python program to count the frequency of words in a file

# To open the text file
f = open('demo.txt', 'r')

# Initialize and empty dictionary to store the frequency count
count=dict()

# To count the frequency of each word in a file
for line in f:
    words=line.split()
    for word in words:
        if word in count:
            count[word]=+1
        else:
            count[word]=1
print(count)