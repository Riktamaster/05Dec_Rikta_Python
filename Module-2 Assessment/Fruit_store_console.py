# Write a program to demonstrate the Fruit Store Console application 

# UDF to initialize the fruit store with an empty stock and empty customer_bought_items
def initialize_fruit_store():
    return {"stock": {},"customer_bought_items": {}}

# UDF to display options for manager menu 
def display_manager_menu():
    print("1. Add Fruit Stock")
    print("2. View Fruit Stock")
    print("3. Update Fruit Stock")
    print("4. Exit")

# UDF to execute manager menu logic
def execute_manager_menu(fruit_store):
    display_manager_menu()
    choice = int(input("Enter your choice:"))
    if choice == 1:
        add_fruit_stock(fruit_store)
    elif choice == 2:
        view_fruit_stock(fruit_store)
    elif choice == 3:
        update_fruit_stock(fruit_store)
    elif choice == 4:
        print("Exiting the Fruit Store Console Application. Goodbye!")
    else:
        print("Invalid choice. Please enter a valid option.")

# UDF to add fruit stock based on user input
def add_fruit_stock(fruit_store):
    fruit_name = str(input("Enter Fruit Name: "))
    quantity = float(input("Enter quantity (in kgs.) to add: "))
    price = float(input("Enter the price per unit: "))

    # To check if the fruit already exists in stock
    if fruit_name in fruit_store["stock"]:
        # Increment the quantity if the fruit already exists
        fruit_store["stock"][fruit_name]["quantity"] += quantity
    else:
        # Add a new entry if the fruit doesn't exist
        fruit_store["stock"][fruit_name] = {"quantity": quantity, "price": price}
    print("Fruit stock added successfully.")
    # Display the updated fruit stock
    view_fruit_stock(fruit_store)

# UDF to view the current fruit stock
def view_fruit_stock(fruit_store):
    # To retrive the value associated with the key 'stock'
    stock = fruit_store.get("stock", {})
    print("Fruit stock:",stock)
    return stock

# UDF to update the quantity and price of a specific fruit in stock
def update_fruit_stock(fruit_store):
    fruit_name = input("Enter Fruit Name to update:")
    new_quantity = float(input("Enter new quantity:"))
    new_price = float(input("Enter new price:"))
    
    if fruit_name in fruit_store["stock"]:
        # Update the quantity of the specified fruit
        fruit_store["stock"][fruit_name]["quantity"] = new_quantity
        # Update the price of the specified fruit
        fruit_store["stock"][fruit_name]["price"] = new_price
        print("Fruit stock updated successfully.")
    else:
        print("Fruit not found in stock.")

# UDF to display options for customer menu
def display_customer_menu():
    print("1. View Fruit Stock")
    print("2. Buy Fruits")
    print("3. Exit")

# UDF to execute customer menu logic
def execute_customer_menu(fruit_store):
    display_customer_menu()
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            view_fruit_stock(fruit_store)
        elif choice == 2:
            buy_fruits(fruit_store)
        elif choice == 3:
            print("Thank you for visiting. Have a great day!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# UDF to allow customers to buy fruits
def buy_fruits(fruit_store):
    fruit_name = input("Enter the fruit name you want to buy: ")
    quantity = float(input("Enter the quantity to buy: "))
    stock = view_fruit_stock(fruit_store)  # Call view_fruit_stock to retrieve the stock

    if fruit_name in stock:
        price = stock[fruit_name]["price"]
        total_cost = quantity * price
        print(f"Total Cost: Rs.{total_cost}")

        confirmation = input("Confirm purchase? (yes/no): ")
        if confirmation.lower() == 'yes':
            # Check if there is enough quantity in stock
            if stock[fruit_name]["quantity"] >= quantity:
                # Update customer bought items and deduct from the stock
                update_customer_bought_items(fruit_name, quantity, total_cost, fruit_store)
                print(f"You have successfully bought {quantity} {fruit_name}(s) for Rs.{total_cost}.")
            else:
                print(f"Insufficient quantity in stock. Available: {stock[fruit_name]['quantity']}")
        else:
            print("Purchase cancelled.")
    else:
     print("Fruit not found in stock.")

# UDF to update the customer_bought_items dictionary with the purchased items
def update_customer_bought_items(fruit_name, quantity, total_cost, fruit_store):
    # Retrieve the customer's bought items or initialize an empty dictionary if it doesn't exist
    customer_bought_items = fruit_store.get("customer_bought_items", {})
    
    if fruit_name in customer_bought_items:
         # If the fruit is already in the customer's bought items, update the quantity and total cost
        customer_bought_items[fruit_name]["quantity"] += quantity
        customer_bought_items[fruit_name]["total_cost"] += total_cost
    else:
         # If the fruit is not in the customer's bought items, add a new entry
        customer_bought_items[fruit_name] = {"quantity": quantity, "total_cost": total_cost}
     # Update the customer's bought items in the fruit store
    fruit_store["customer_bought_items"] = customer_bought_items

# Main program to run the Fruit Store Console Application until the user chooses to exit
store = initialize_fruit_store()
role = input("Enter your role (Manager, Customer, or Exit to end): ").lower()

while role != 'exit':
    # Manager role
    if role == 'manager':
        execute_manager_menu(store)
        more_operations = input("Do you want to perform more operations? (yes/no): ").lower()
        if more_operations != 'yes':
            print("Exiting the Manager Menu.")
        else:
            continue
    # Customer role
    elif role == 'customer':
        execute_customer_menu(store)
    # Invalid role
    else:
        print("Invalid role. Please enter 'Manager' or 'Customer'.")
    # Prompt for the next role or exit
    role = input("Enter your role (Manager, Customer, or Exit to end): ").lower()
print("Exiting the Fruit Store Console Application. Goodbye!")