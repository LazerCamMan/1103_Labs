def get_valid_input():
    rejected_entry = 0
    while True:
        stock_name = input("Enter Item Name (or type 'quit' to exit): ")
        if stock_name == 'quit':
            return (False, 0, 0, rejected_entry)
        stock_quantity = input("Enter Item Stock (or type 'quit' to exit): ")
        if stock_quantity == 'quit':
            return (False, 0, 0, rejected_entry)
        elif stock_quantity.isdigit() and int(stock_quantity) >= 0:
            return (True, stock_name, int(stock_quantity), rejected_entry)
        else:
            print("Please enter a valid positive integer for stock quantity or 'quit' to exit")
            rejected_entry += 1
            continue

def process_delivery(current_total, new_stock):
    if current_total + new_stock > 500:
        print("Overstock Alert! Total inventory exceeds 500 units.")
        return (False, current_total)
    else:
        tax = calculate_tax(new_stock)
        print("Current stock: ", current_total + new_stock)
        print("Tax for this specific delivery: " + str(tax))
        return (True, current_total + new_stock)

def calculate_tax(amount):
    tax = amount * 0.10
    return tax

def generate_report(current_total, total_rejected_entries):
    print("Final Report:")
    print("Current stock: " + str(current_total))
    print("No of Rejected Entries: " + str(total_rejected_entries))

def load_inventory():
    current_inventory = []
    try:
        with open("inventory.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                current_inventory.append(line.split(","))
    except FileNotFoundError:
        with open("inventory.txt", "w") as file:
            pass
    print("Current Orders:" + "\n")
    for item in current_inventory:
        print(f"{item[0]}" + f"{item[1]}" + f"{item[2]}")
    return current_inventory

def main():
    current_total = 0
    total_rejected_entries = 0
    inventory = load_inventory()
    while True:
        valid, stock_name, stock_quantity, rejected_entry = get_valid_input()
        total_rejected_entries += rejected_entry
        print(stock_name, stock_quantity)
        if not valid:
            generate_report(current_total, total_rejected_entries)
            break

        success, current_total = process_delivery(current_total, stock_quantity)
        if not success:
            break
            


main()