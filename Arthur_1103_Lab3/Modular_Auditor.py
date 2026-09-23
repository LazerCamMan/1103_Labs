inventory = int(0)
rejected_entry = int(0)

def get_valid_input():
    while True:
        stocked = input("How much would you like to stock? Type 'quit' to exit: ")
        if stocked == 'quit':
            return (False, None)
        elif stocked.isdigit() and int(stocked) >= 0:
            return (True, int(stocked))
        else:
            print("Please enter a valid positive integer for stock quantity or 'quit' to exit")
            continue

while True:
    valid, stocked = get_valid_input()
    if stocked == 'quit':
        print("Current stock: " + str(inventory) + "\nNo of Rejected Entries: " + str(rejected_entry))
        break
    else:
        inventory = inventory + int(stocked)
    if inventory > 500:
        rejected_entry = rejected_entry + 1
        print("Overstock Alert! Total inventory exceeds 500 units.")
        break
    print("Current stock:", inventory)