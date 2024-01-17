# 0  Inventory
inventory = {
    'item1': {'id': 1, 'name': '商品1', 'price': 20.99, 'inventory': 2},
    'item2': {'id': 2, 'name': '商品2', 'price': 15.49,'inventory': 3},
    'item3': {'id': 3, 'name': '商品3', 'price': 30.0, 'inventory': 4}
}

# 1 Function to add an item to the inventory
def add_item(item_id, name, quantity, price):
    if item_id not in inventory:
        inventory[item_id]['quantity'] += quantity
    else:
        inventory[item_id] = {'name': name, 'quantity': quantity, 'price': price}

# 2 Function to view all items in the inventory
def view_inventory():
    return inventory

add_item(1, "商品4", 19.99, 9)
add_item(2, "商品5", 21.99, 7)

print(view_inventory)

# 3 Function to update the quantity of an existing item in the inventory
def update_item(item,quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

# 4 Main function to manage the inventory
def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. Add_Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

# 5 Entry point of the program
if __name__ == "__main__":
    manage_inventory()