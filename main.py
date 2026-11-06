from product import Product
from inventory import Inventory
from filehandling import FileHandling
from physicalproduct import PhysicalProduct
from digitalproduct import DigitalProduct

#Prints main header
def print_header():
    print("=======================\n" + "INVENTORY MANAGER\n" + "=======================" )
#Prints the main menu options
def print_main_menu():
    print("\n======Main Menu======")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("======================")

def user_input_main_menu_choice():
    try:
        choice = int(input("\nEnter your choice (1-6): "))
        if choice < 1 or choice > 6:
            print("\nInvalid choice. Please enter a number between 1 and 6.")
            return user_input_main_menu_choice()
    except ValueError:
        print("\nInvalid input. Please enter a number.")
        return user_input_main_menu_choice()
    return choice

#======================Add Product Related Functions========================================================
def add_product_user_input_product_info(inventory):
    print("\nAdd New Product\n" + "-------------------------------")
    new_id = get_next_id(inventory)
    print("Product ID: ", new_id)
    product_type_flag = user_input_product_type()#Returns d if digital, p if phsyical
    name = input("Enter product name: ")
    price = user_input_product_price()
    stock = user_input_product_stock()

    if product_type_flag == "d":
        add_digital_product(new_id, name, price, stock, inventory)
    elif product_type_flag == "p":
        add_physical_product(new_id, name, price, stock, inventory)


def add_physical_product(product_id, name, price, stock, inventory):
    weight = user_input_product_weight()
    product = PhysicalProduct(product_id, name, price, stock, weight)
    inventory.add_product(product)
    print("\nProduct added to session. Select Save to commit product to database")

def add_digital_product(product_id, name, price, stock, inventory):
    download_size = user_input_product_download_size()
    product = DigitalProduct(product_id, name, price, stock, download_size)
    inventory.add_product(product)
    print("\nProduct added to session. Select Save to commit product to database")

def user_input_product_type(): #Returns d if digital, p if phsyical
    while True:
        product_type = input("Enter product type (d/p): ").strip().lower()
        if product_type in ("d", "p"):
            return product_type
        print("Invalid input (d/p)")

def get_next_id(inventory):
    products = inventory.get_products()
    if not products:
        return "P001"
    highest = max(int(p.get_product_id()[1:]) for p in products)
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

def user_input_product_weight():
    try:
        weight = float(input("Enter product weight: "))
        if weight < 0:
            print("\nInput a valid weight. (Weight cannot be negative)")
            return user_input_product_weight()
        return weight    
    except ValueError:
        print("\nInput a valid weight. (Float Number)")
        return user_input_product_weight()

def user_input_product_download_size():
    try:
        download_size = float(input("Enter product download size: "))
        if download_size < 0:
            print("\nInput a valid download size. (Download size cannot be negative)")
            return user_input_product_download_size()
        return download_size    
    except ValueError:
        print("\nInput a valid download size. (Float Number)")
        return user_input_product_download_size()
#====================================================================================================

#======================Update Stock related functions (builds off previous functions)======================
def update_stock_quantity_main_function(inventory):
    print("\nUpdate Product Stock\n" + "-------------------------------")
    result = return_product_based_on_user_product_id(inventory)

    if not result:
        print("\nProduct not found")
        update_stock_quantity_main_function(inventory)
    if result:
        result.display_information()
        updated_stock_quantity = user_input_product_stock()
        result.update_stock(updated_stock_quantity)
        print("\nStock updated in session. Select Save to commit product to database")


def return_product_based_on_user_product_id(inventory):
        user_inputted_product_id = input("Enter Product ID: ")
        result = inventory.search_product(user_inputted_product_id)
        return result
#====================================================================================================
#======================Search Stock related functions (builds off previous functions)======================
def search_stock_quantity_main_function(inventory):
    print("\nSearch Product\n" + "-------------------------------")
    result = return_product_based_on_user_product_id(inventory)

    if not result:
        print("\nProduct not found")
        search_stock_quantity_main_function(inventory)
    if result:
        result.display_information()
        print()
        result.get_fulfilment_info()
#====================================================================================================


def main():
    print_header()
    file_handler = FileHandling()
    inventory = file_handler.load_inventory()
    print_main_menu()
    user_menu_choice = user_input_main_menu_choice()

    while True:
        if user_menu_choice == 1:
            inventory.display_all()
            user_menu_choice = user_input_main_menu_choice()
        elif user_menu_choice == 2:
            add_product_user_input_product_info(inventory)
            user_menu_choice = user_input_main_menu_choice()
        elif user_menu_choice == 3:
            update_stock_quantity_main_function(inventory)
            user_menu_choice = user_input_main_menu_choice()
        elif user_menu_choice == 4:
            search_stock_quantity_main_function(inventory)
            user_menu_choice = user_input_main_menu_choice()
        elif user_menu_choice == 5:
            file_handler.save_inventory(inventory)
            user_menu_choice = user_input_main_menu_choice()
        elif user_menu_choice == 6:
            file_handler.save_inventory(inventory)
            print("Exiting the Program")
            break


#===========================================================================================================
main()