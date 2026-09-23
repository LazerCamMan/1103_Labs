inventory = int(0)
rejected_entry = int(0)
while True:
    stocked = input("How much would you like to stock? Type 'quit' to exit: ")
    if stocked == 'quit':
        print("Current stock: " + str(inventory) + "\nNo of Rejected Entries: " + str(rejected_entry))
        break
    elif stocked.isdigit() == False or int(stocked) < 0:
        print("Please enter a valid positive integer for stock quantity or 'quit' to exit")
        rejected_entry = rejected_entry + 1
        continue
    else:
        inventory = inventory + int(stocked)
    if inventory > 500:
        rejected_entry = rejected_entry + 1
        print("Overstock Alert! Total inventory exceeds 500 units.")
        break
    print("Current stock:", inventory)