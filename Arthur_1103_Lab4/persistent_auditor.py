def get_valid_input(inventory):
    rejected_entry = 0
    while True:
        stock_name = input("Enter Item Name (or type 'quit' to exit): ").strip()
        if stock_name.lower() == "quit":
            return False, None, rejected_entry
        if not stock_name:
            print("Item name can't be empty.")
            rejected_entry += 1
            continue

        stock_quantity = input("Enter Item Stock (or type 'quit' to exit): ")
        if stock_quantity == 'quit':
            return (False, 0, rejected_entry)
        elif stock_quantity.isdigit() and int(stock_quantity) >= 0:
            new_stock = [str(len(inventory) + 1001), stock_name, stock_quantity]
            return (True, new_stock, rejected_entry)
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

def generate_report(session_total, total_rejected_entries):
    print("Final Report:")
    print("Total Stock added this session: " + str(session_total))
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
        print(f"{item[0]}", f"{item[1]}", f"{item[2]}")
    print("\n")
    return current_inventory

def save_inventory(new_stock):
    with open("inventory.txt", "a") as file:
        file.write("\n" + ",".join(new_stock))
    print("\n" + "New Order added:")
    print(f"{new_stock[0]}", f"{new_stock[1]}", f"{new_stock[2]}" + "\n")
    print("Order(s) added successfully to inventory.txt!" + "\n")


def main():
    session_total = 0
    total_rejected_entries = 0
    inventory = load_inventory()
    while True:
        valid, new_stock, rejected_entry = get_valid_input(inventory)
        total_rejected_entries += rejected_entry
        if not valid:
            generate_report(session_total, total_rejected_entries)
            break

        inventory.append(new_stock)
        save_inventory(new_stock)
        session_total += int(new_stock[2])



main()