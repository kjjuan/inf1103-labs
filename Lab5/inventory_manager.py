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


inventory = []
add_product(inventory, "P001", "Laptop", 1200.00, 15)
add_product(inventory, "P002", "Mouse", 25.50, 40)
add_product(inventory, "P003", "Keyboard", 45.00, 25)

display_all(inventory)
