import json


#===========================MAIN FUNCTION============================================================
def main():
    current_inventory = load_inventory()
    print_header()
    print_main_menu()
    user_menu_choice = main_menu_choice()
    execute_user_choice_selection(user_menu_choice, current_inventory)
#====================================================================================================



#=======================Display Function========================================================
def display_inventory_main_function(inventory):
    print("Current Inventory:\n" + "-------------------------------")
    for item in inventory:
        print(f"ID: {item['ID']} | Name: {item['Name']} | Price: ${item['Price']:.2f} | Stock: {item['Stock']}")
    print("-------------------------------\n")
#====================================================================================================


#======================add product Related Functions========================================================
def add_product_main_function(inventory):
    print("Add New Product\n" + "-------------------------------")
    new_id = get_next_id(inventory)
    print("Product ID: ", new_id)

    name = input("Enter product name: ")
    price = user_input_product_price()
    stock = user_input_product_stock()

    inventory.append({'ID': new_id, 'Name': name, 'Price': price, 'Stock': stock})
    print("Product added to session. Select Save to commit product to database\n")

def get_next_id(inventory):
    if not inventory:
        return "P001"
    highest = max(int(item["ID"][1:]) for item in inventory)
    return f"P{highest + 1:03d}"

def user_input_product_price():
    try:
        price = float(input("Enter product price: $"))
        if price < 0:
            print("\nInput a valid price. (Price cannot be negative)")
            return user_input_product_price()
        return price    
    except ValueError:
        print("\nInput a valid price. (Float Number)")
        return user_input_product_price()

def user_input_product_stock():
    try:
        stock = int(input("Enter product stock quantity: "))
        if stock < 0:
            print("\nInput a valid stock quantity. (Stock quantity cannot be negative)")
            return user_input_product_stock()
        return stock
    except ValueError:
        print("\nInput a valid stock quantity. (Integer Number)")
        return user_input_product_stock()

#====================================================================================================

#======================Search and Update Stock Related Functions=================================================
def update_stock_quantity_main_function(inventory):
    print("\nUpdate Product Stock\n" + "-------------------------------")
    result = search_for_product_based_on_user_inputted_product_ID(inventory)
    if not result:
        print("\nProduct not found\n")
        update_stock_quantity_main_function(inventory)
    if result:
        print_product_information(result)
        update_stock_number_based_on_user_input(result)
        print("\nStock updated in session. Select Save to commit product to database\n")

def update_stock_number_based_on_user_input(product_dict):
    new_stock = user_input_product_stock()
    if product_dict:
        product_dict["Stock"] = new_stock


def search_for_product_based_on_user_inputted_product_ID(inventory):
    product_id = input("Input Product ID: ")
    for item in inventory:
        if item["ID"] == product_id:
            return item
    return None

def search_and_print_product_main_function(inventory):
    print("\nSearch Product\n" + "-------------------------------")
    result = search_for_product_based_on_user_inputted_product_ID(inventory)
    if not result:
        print("\nProduct not found")
        update_stock_quantity_main_function(inventory)
    if result:
        print_product_information(result)

def print_product_information(product_information):
    print("\nProduct Information:\n" + "-------------------------------")
    print(f"ID: {product_information['ID']}")
    print(f"Name: {product_information['Name']}")
    print(f"Price: $ {product_information['Price']:.2f}")
    print(f"Stock: {product_information['Stock']}")
    print("-------------------------------\n")
#====================================================================================================

#=====================DATA BASE HANDLING============================================================
def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            current_inventory = json.load(file)
            return current_inventory
    except FileNotFoundError:
        with open("inventory.json", "w") as file:
            json.dump([], file)
        return []

def save_inventory():
    pass


#====================================================================================================

#=====================USER INPUT HANDLING============================================================
def execute_user_choice_selection(user_menu_choice, inventory):
    if user_menu_choice == 1:
        display_inventory_main_function(inventory)
        user_menu_choice = main_menu_choice()
        execute_user_choice_selection(user_menu_choice, inventory)
    elif user_menu_choice == 2:
        add_product_main_function(inventory)
        user_menu_choice = main_menu_choice()
        execute_user_choice_selection(user_menu_choice, inventory)
    elif user_menu_choice == 3:
        update_stock_quantity_main_function(inventory)
        user_menu_choice = main_menu_choice()
        execute_user_choice_selection(user_menu_choice, inventory)
    elif user_menu_choice == 4:
        search_and_print_product_main_function(inventory)
        user_menu_choice = main_menu_choice()
        execute_user_choice_selection(user_menu_choice, inventory)
    elif user_menu_choice == 5:
        search_and_print_product(inventory)
        user_menu_choice = main_menu_choice()
        execute_user_choice_selection(user_menu_choice, inventory)
    elif user_menu_choice == 6:
        print("Exiting the Program")    
#====================================================================================================




#======================HEADER AND MENU FUNCTIONS=====================================================
#Prints main header
def print_header():
    print("=======================\n" + "INVENTORY MANAGER\n" + "=======================\n" )
#Prints the main menu options
def print_main_menu():
    print("======Main Menu======")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("======================\n")
#Gets the user input for the main menu,validates and returns it
def main_menu_choice():
    try:
        choice = int(input("Enter your choice (1-6): "))
        if choice < 1 or choice > 6:
            print("\nInvalid choice. Please enter a number between 1 and 6.")
            return main_menu_choice()
    except ValueError:
        print("\nInvalid input. Please enter a number.")
        return main_menu_choice()
    return choice
#====================================================================================================








main()
