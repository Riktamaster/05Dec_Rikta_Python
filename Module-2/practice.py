# To get a number of terms from the user
n = int(input("Enter number of terms: "))

# Initializing first two terms
t1, t2 = 0, 1

# Displaying the first two terms
print(f"Fibonacci series: {t1}, {t2}", end=", ")

# Generating Fibonacci series
for i in range(3, n + 1):
    next_term = t1 + t2
    print(next_term, end=", ")
    t1, t2 = t2, next_term
