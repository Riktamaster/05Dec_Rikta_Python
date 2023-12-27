#Write a Python program to get Fibonacci series of given range

#To get number of terms from user
n=int(input("Enter number of terms:"))

#For displaying term 1 and term 2
t1=0
t2=1
print(f"Fibonacci series: {t1}, {t2}", end=", ")

#To get Fibonacci series of entered terms
for i in range(3,n+1):
    next_term=t1+t2
    print(next_term, end=", ")
    t1=t2
    t2=next_term

