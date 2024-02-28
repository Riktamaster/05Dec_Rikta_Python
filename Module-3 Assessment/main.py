import pymysql
from banker import Banker # to import module Banker from banker.py
from customer import Customer # to import module Customer from customer.py

# To connect the main program to database named 'bankingapp'
try:
    dbcon=pymysql.connect(host='localhost',user='root',password='',database='bankingapp')
    print("Database created!")
except Exception as e:
    print(e)

# To create cusrsor for the database
cr=dbcon.cursor()

# To create table named Customer
ctbl_create="CREATE TABLE Customer(ID integer primary key auto_increment, Name text, Account_no bigint UNIQUE NOT NULL, Age int, Gender text,Mobile_no bigint UNIQUE NOT NULL, E_mail text, password text, Balance bigint)"
try:
    cr.execute(ctbl_create)
    print("Customer table created!")
except Exception as e:
    print(e)

# Main program
print("----------------------")
print("Welcome to Python Bank")
print("----------------------")
while True:
    print("1. Banker")
    print("2. Customer")
    print("3. Exit")

    choice = int(input("Enter number(1-3) to choose your role:"))

    if choice == 1:
        banker = Banker()

        print("1. Register")
        print("2. Login")
        print("3. Update all Customers")
        print("4. View all Customers")
        print("5. Delete all Customers")

        operation = int(input("Enter your choice of operation (1-5):"))

        if operation == 1:
        # Registration for banker
            name = input("Enter customer's name: ")
            account_no = input("Enter customer's account number: ")
            age = input("Enter customer's age: ")
            gender = input("Enter customer's gender: ")
            mobile_no = input("Enter customer's mobile number: ")
            email = input("Enter customer's email: ")
            password = input("Enter password: ")
            balance=input("Enter balance:")
            banker.register_customer(name, account_no, age, gender, mobile_no, email, password,balance )

        elif operation == 2:
        # Login for banker
            email = input("Enter your email: ")
            password = input("Enter your password: ")

            banker.login(email, password)

        elif operation == 3:
        # Update all customers for banker 
            banker.update_all_customers()

        elif operation == 4:
        # View all customers for banker
            banker.view_all_customers()

        elif operation == 5:
        # Delete all customers for banker
            banker.delete_all_customers()

        else:
            print("Invalid operation. Please enter a number between 1 and 5.")

    elif choice == 2:
        
        print("1. Register")
        print("2. Login")
        print("3. Withdraw amount")
        print("4. Deposit amount")
        print("5. View Balance")
        operation = int(input("Enter your choice of operation (1-5):"))

        if operation == 1:
        # Register for customer
            customer = Customer(0)
            name = input("Enter your name: ")
            account_no=int(input("Enter your account number:"))
            age = int(input("Enter your age: "))
            gender = input("Enter your gender: ")
            mobile_no = input("Enter your mobile number: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            balance = float(input("Enter initial balance: "))
            customer.register(name, account_no, age, gender, mobile_no, email, password, balance)

        # Login for customer
        elif operation == 2:
            account_no = int(input("Enter your account number: "))
            customer = Customer(account_no)
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            customer.login(email, password)

        # Withdrawal for customer
        elif operation == 3:
            account_no = int(input("Enter your account number: "))
            customer = Customer(account_no)
            customer.withdraw()

        # Deposition for customer
        elif operation == 4:
            account_no = int(input("Enter your account number: "))
            customer = Customer(account_no)
            customer.deposit()
            
        # View balance for customer
        elif operation == 5:
            account_no = int(input("Enter your account number: "))
            customer = Customer(account_no)
            customer.view_balance()
        else:
            print("Invalid operation. Please enter a number between 1 and 5.")
    
    elif choice == 3:
        print("Exiting the Python Bank application. Thank you!")

    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
        break

    con = input("Do you want to continue(yes/no)?:")
    if con.lower() == 'no':
        print("Thank you for visiting!")
        break