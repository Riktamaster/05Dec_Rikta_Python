import pymysql

try:
    dbcon=pymysql.connect(host='localhost',user='root',password='',database='bankingapp')
    print("Database created!")
except Exception as e:
    print(e)

cr=dbcon.cursor()

import pymysql

class Account:
    def __init__(self, account_no):
        self.Account_no = account_no

    def get_balance(self):
        try:
            cr.execute(f"SELECT Balance FROM Customer WHERE Account_no={self.Account_no}")
            balance = cr.fetchone()

            if balance:
                return balance[0]
            else:
                return 0
        except Exception as e:
            print(e)
            return 0

class Customer(Account):
    #UDF to register for customer
    def register(self, Name, Account_no, Age, Gender, Mobile_no, E_mail, password, balance):
        try:
            cr.execute(f"SELECT * FROM Customer WHERE Mobile_no={Mobile_no}")
            existing_customer = cr.fetchone()

            if existing_customer:
                print("Error: Customer with this Mobile number already exists.")
            else:
                cr.execute(f"INSERT INTO Customer (Name, Account_no, Age, Gender, Mobile_no, E_mail, password, Balance) VALUES ('{Name}', '{Account_no}', '{Age}', '{Gender}', '{Mobile_no}', '{E_mail}', '{password}', '{balance}')")
                dbcon.commit()
                print("Customer registered successfully!")
        except Exception as e:
            print(e)

    #UDF for login of customer
    def login(self, E_mail, password):
        try:
            cr.execute(f"SELECT * FROM Customer WHERE E_mail='{E_mail}' AND password='{password}'")
            customer = cr.fetchone()
            if customer:
                print("Login successful.")
            else:
                print("Error! Invalid credentials.")
        except Exception as e:
            print(e)

    #UDF to withdraw for customer
    def withdraw(self):
        try:
            amount = float(input("Enter the amount to withdraw: "))
            balance = self.get_balance()

            if amount > balance:
                print("Error: Insufficient funds.")
            else:
                new_balance = balance - amount
                cr.execute(f"UPDATE Customer SET Balance={new_balance} WHERE Account_no={self.Account_no}")
                dbcon.commit()
                print(f"Withdrawal successful. New balance: {new_balance}")

        except Exception as e:
            print(e)

    #UDF to deposit for customer
    def deposit(self):
        try:
            amount = float(input("Enter the amount to deposit: "))
            balance = self.get_balance()
            new_balance = balance + amount
            cr.execute(f"UPDATE Customer SET Balance={new_balance} WHERE Account_no={self.Account_no}")
            dbcon.commit()
            print(f"Deposit successful. New balance: {new_balance}")
        except Exception as e:
            print(e)

    #UDF to view balance of customer
    def view_balance(self):
        try:
            balance = self.get_balance()

            print(f"Current balance for Account {self.Account_no}: {balance}")
        except Exception as e:
            print(e)