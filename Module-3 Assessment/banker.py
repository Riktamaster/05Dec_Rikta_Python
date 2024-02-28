import pymysql

try:
    dbcon=pymysql.connect(host='localhost',user='root',password='',database='bankingapp')
    print("Database created!")
except Exception as e:
    print(e)

cr=dbcon.cursor()
class Banker:
#UDF to register customer
    def register_customer(self, Name, Account_no, Age, Gender, Mobile_no, E_mail, password,balance):
        try:
            cr.execute(f"SELECT * FROM Customer WHERE Mobile_no={Mobile_no}")
            existing_customer=cr.fetchone()
            if existing_customer:
                print("Error:Customer with this mobile number already exists.")
            else:
                cr.execute(f"INSERT INTO Customer (Name,Account_no,Age,Gender,Mobile_no,E_mail,password,Balance) VALUES ('{Name}','{Account_no}','{Age}','{Gender}','{Mobile_no}','{E_mail}','{password}','{balance}')")
                dbcon.commit()
                print("Customer registered successfully!")
        except Exception as e:
            print(e)

    #UDF for Login
    def login(self, E_mail, password):
        try:
            cr.execute(f"SELECT * FROM Customer WHERE E_mail='{E_mail}' AND password='{password}'")
            customer=cr.fetchone()
            if customer:
                print("Login successful.")
            else:
                print("Error! Invalid credentials.")
        except Exception as e:
            print(e)
    
    # UDF to update all customers
    def update_all_customers(self):
        try:
            cr=dbcon.cursor()
            print("1. Update Name")
            print("2. Update Account number")
            print("3. Update Age")
            print("4. Update Gender")
            print("5. Update Mobile number")
            print("6. Update E_mail address")
            print("7. Update password")
            print("8. Update Balance")
            choice=int(input("Enter number(1-8) to update any information:"))
            if choice==1:
                new_name=input("Enter new name for all customers:")
                cr.execute(f"UPDATE Customer SET Name='{new_name}'")
                dbcon.commit()
            elif choice==2:
                new_acc_no=input("Enter new account number for all customers:")
                cr.execute(f"UPDATE Customer SET Account_no={new_acc_no}")
                dbcon.commit()
            elif choice==3:
                new_age=input("Enter new age for all customers:")
                cr.execute(f"UPDATE Customer SET Age={new_age}")
                dbcon.commit()
            elif choice==4:
                new_gender=input("Enter new gender for all customers:")
                cr.execute(f"UPDATE Customer SET Gender='{new_gender}'")
                dbcon.commit()
            elif choice==5:
                new_mo_no=input("Enter new Mobile number for all customers:")
                cr.execute(f"UPDATE Customer SET Mobile_no={new_mo_no}")
                dbcon.commit()
            elif choice==6:
                new_email=input("Enter new E_mail for all customers:")
                cr.execute(f"UPDATE Customer SET E_mail='{new_email}'")
                dbcon.commit()
            elif choice==7:
                new_pw=input("Enter new password for all customers:")
                cr.execute(f"UPDATE Customer SET password='{new_pw}'")
                dbcon.commit()
            elif choice==8:
                new_bal=input("Enter new balance for all customers:")
                cr.execute(f"UPDATE Customer SET Balance={new_bal}")
                dbcon.commit()
                print("All customers updated successfully!")
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")
        except Exception as e:
            print(e)
    
    # UDF to view all customers
    def view_all_customers(self):
        try:
            cr.execute("SELECT * FROM Customer")
            all_customers = cr.fetchall()

            if all_customers:
                print("\nAll Customers:")
                for customer in all_customers:
                    print(f"ID:{customer[0]},Name:{customer[1]},Account_no:{customer[2]},Age:{customer[3]},Gender:{customer[4]},Mobile_no:{customer[5]},E_mail:{customer[6]},password:{customer[7]},Balance:{customer[8]}")
            else:
                print("No customers found.")
        except Exception as e:
            print(e)
    
    # UDF to delete all customers
    def delete_all_customers(self):
        try:
            confirm = input("Are you sure you want to delete all customers? (Y/N): ")
            if confirm.upper() == 'Y':
                # Delete all customers from the database
                cr.execute("DELETE FROM Customer")
                dbcon.commit()
                print("All customers deleted successfully.")
            else:
                print("Deletion canceled.")
        except Exception as e:
            print(e)