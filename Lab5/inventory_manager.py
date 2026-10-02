import json
import os

INVENTORY_FILE = "inventory.json"


def display_all(inventory):
    """
    In:  inventory (list of dict)
    Out: (nothing) - prints every product in the inventory
    """
    print("\nCurrent Inventory")
    print("-" * 48)

    if len(inventory) == 0:
        print("Inventory is empty.")

    for product in inventory:
        print(f"ID: {product['id']} | Name: {product['name']} | "
              f"Price: ${product['price']:.2f} | Stock: {product['stock']}")

    print("-" * 48)


def search_product(inventory, product_id):
    """
    In:  inventory (list of dict), product_id (str)
    Out: the matching product (dict), or None if it is not found
    """
    for product in inventory:
        if product["id"].upper() == product_id.upper():
            return product

    return None


def add_product(inventory, product_id, name, price, stock):
    """
    In:  inventory (list of dict), product_id (str), name (str),
         price (float), stock (int)
    Out: True if the product was added, False if the ID already exists
    """
    if search_product(inventory, product_id) is not None:
        return False

    product = {
        "id": product_id.upper(),
        "name": name,
        "price": price,
        "stock": stock
    }
    inventory.append(product)
    return True


def update_stock(inventory, product_id, new_stock):
    """
    In:  inventory (list of dict), product_id (str), new_stock (int)
    Out: True if the stock was updated, False if the product was not found
    """
    product = search_product(inventory, product_id)

    if product is None:
        return False

    product["stock"] = new_stock
    return True


def load_inventory():
    """
    In:  (nothing)
    Out: the list of products read from INVENTORY_FILE,
         or an empty list if the file does not exist yet
    """
    if not os.path.exists(INVENTORY_FILE):
        print(f"{INVENTORY_FILE} not found.")
        print("Starting with an empty inventory.")
        return []

    print(f"{INVENTORY_FILE} found.")
    with open(INVENTORY_FILE, "r") as file:
        inventory = json.load(file)

    print("Inventory loaded successfully.")
    return inventory


def save_inventory(inventory):
    """
    In:  inventory (list of dict)
    Out: (nothing) - writes the inventory to INVENTORY_FILE as JSON
    """
    with open(INVENTORY_FILE, "w") as file:
        json.dump(inventory, file, indent=4)


def get_valid_int(prompt):
    """
    In:  prompt (str)
    Out: a non-negative int entered by the user (asks again until valid)
    """
    while True:
        entry = input(prompt).strip()
        if entry.isdigit():
            return int(entry)
        print("Error: please enter a valid whole number.")


def get_valid_price(prompt):
    """
    In:  prompt (str)
    Out: a non-negative float entered by the user (asks again until valid)
    """
    while True:
        entry = input(prompt).strip()
        try:
            price = float(entry)
        except ValueError:
            print("Error: please enter a valid price.")
            continue

        if price < 0:
            print("Error: price cannot be negative.")
            continue

        return price


def show_menu():
    """
    In:  (nothing)
    Out: (nothing) - prints the menu options
    """
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


print("=" * 40)
print("INVENTORY MANAGEMENT SYSTEM")
print("=" * 40)
print()

inventory = load_inventory()
show_menu()

while True:
    option = input("\nEnter option: ").strip()

    if option == "1":
        display_all(inventory)

    elif option == "2":
        print("\nAdd New Product")
        product_id = input("Product ID: ").strip()
        if product_id == "":
            print("\nError: product ID cannot be empty.")
            continue
        if search_product(inventory, product_id) is not None:
            print(f"\nError: product {product_id.upper()} already exists.")
            continue
        name = input("Product Name: ").strip()
        price = get_valid_price("Price: ")
        stock = get_valid_int("Stock Quantity: ")

        add_product(inventory, product_id, name, price, stock)
        print("\nProduct added successfully!")

    elif option == "3":
        print("\nUpdate Stock")
        product_id = input("Enter Product ID: ").strip()
        product = search_product(inventory, product_id)

        if product is None:
            print("\nProduct not found.")
            continue

        print("\nProduct Found:")
        print(f"Name: {product['name']}")
        print(f"Current Stock: {product['stock']}")
        new_stock = get_valid_int("\nNew Stock Quantity: ")

        update_stock(inventory, product_id, new_stock)
        print("\nStock updated successfully!")

    elif option == "4":
        print("\nSearch Product")
        product_id = input("Enter Product ID: ").strip()
        product = search_product(inventory, product_id)

        if product is None:
            print("\nProduct not found.")
            continue

        print("\nProduct Found")
        print("-" * 48)
        print(f"ID: {product['id']}")
        print(f"Name: {product['name']}")
        print(f"Price: ${product['price']:.2f}")
        print(f"Stock: {product['stock']}")
        print("-" * 48)

    elif option == "5":
        print("\nSaving inventory...")
        save_inventory(inventory)
        print(f"Inventory saved successfully to {INVENTORY_FILE}.")

    elif option == "6":
        print("\nSaving inventory before exit...")
        save_inventory(inventory)
        print("Inventory saved successfully.")
        print("\nThank you for using Inventory Management System.")
        print("Program terminated.")
        break

    else:
        print("Invalid option. Please enter a number from 1 to 6.")
