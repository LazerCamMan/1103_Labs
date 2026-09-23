def get_valid_input():
    while True:
        new_stock = input("How much would you like to stock? Type 'quit' to exit: ")
        if new_stock == 'quit':
            return (False, new_stock)
        elif new_stock.isdigit() and int(new_stock) >= 0:
            return (True, int(new_stock))
        else:
            print("Please enter a valid positive integer for stock quantity or 'quit' to exit")
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

def main():
    current_total = 0
    rejected_entry = 0
    while True:
        valid, stocked = get_valid_input()
        if not valid:
            print("Current stock: " + str(current_total) + "\nNo of Rejected Entries: " + str(rejected_entry))
            break

        success, current_total = process_delivery(current_total, stocked)
        if not success:
            break
            


main()