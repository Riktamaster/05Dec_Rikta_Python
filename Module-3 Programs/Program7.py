# Write a python program to find the longest words

# To open the text file
f = open('demo.txt', 'r')

# Initialize longest_word to an empty string
longest_word = ""

for line in f:
    for word in line.split():
        # Strip the word and update longest_word if the current word is longer
        stripped_word = word.strip()
        if len(stripped_word) > len(longest_word):
            longest_word = stripped_word

# Print the longest word in the file
print(f"Longest word in the file: {longest_word}")