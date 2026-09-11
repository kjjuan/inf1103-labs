total_inventory = 0
failed_entries = 0

while True:
    entry = input("Enter stock quantity (or 'quit' to stop): ")

    if entry == "quit":
        break

    if not entry.isdigit():
        print("Error: please enter a valid whole number.")
        failed_entries += 1
        continue

    quantity = int(entry)

    if quantity < 0:
        print("Error: negative numbers are not allowed.")
        failed_entries += 1
        continue

    total_inventory += quantity
    print("Total inventory so far:", total_inventory)

    if total_inventory > 500:
        print("ALERT: Overstock! Inventory exceeded 500 units.")
        break

print("\nTotal Units Processed:", total_inventory)
print("Number of Failed/Rejected Entries:", failed_entries)