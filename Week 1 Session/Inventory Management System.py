# The inventory is stored in a dictionary.
# Keys are item names and values are quantities.

inventory = {} #本生就是字典函数

inventory = {
    'item1': {'id': 1, 'name': '商品1', 'price': 20.99, 'inventory': 2},
    'item2': {'id': 2, 'name': '商品2', 'price': 15.49,'inventory': 3},
    'item3': {'id': 3, 'name': '商品3', 'price': 30.0, 'inventory': 4}
}

# Jordan 的标准答案
inventory = {
    'item1': {'id': 1, 'name': 'Hat', 'price': 20.99, 'inventory': 2},
    'item2': {'id': 2, 'name': 'Shoes', 'price': 15.49,'inventory': 3},
    'item3': {'id': 3, 'name': '商品3', 'price': 30.0, 'inventory': 4}
}


--- 
#1 Function to add an item to the inventory
def add_item(item, quantity):
    # Implementation Instructions:
    # 1. Check if the item exists in the inventory dictionary.
    # 2. If it does, increase its quantity.
    # 3. If not, add the item to the inventory with the given quantity.
    pass

def add_item(item_id, name, quantity, price):
    if item_id not in inventory:
        inventory[item_id]['quantity'] += quantity  # aka:inventory[item] + quantity= inventory[item]quantity
    else:
        inventory[item_id] = {'name': name, 'quantity': quantity, 'price': price}


#2 Function to view all items in the inventory
def view_inventory():
    # Implementation Instructions:
    # 1. Loop through the inventory dictionary.
    # 2. Print each item's name and its quantity.
    pass

def view_inventory():
    return inventory



print(view_inventory)

# 2 Jordan 的标准答案
def view_inventory():
    for item_id, quantity in inventory.items():
    print(f"{item}, {quantity}" )

#3 Function to update the quantity of an existing item in the inventory
def update_item(item, quantity):
    # Implementation Instructions:
    # 1. Check if the item exists in the inventory.
    # 2. If it does, update its quantity.
    # 3. If the item doesn't exist, print a message indicating it's not found.
    pass

def update_item(item,quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

# Jordan 
def update_item(item,quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

#4 Main function to manage the inventory
def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. Add_Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        # Process the user's choice
        # Implementation Instructions:
        # 1. If the choice is '1', prompt the user to enter an item name and quantity,
        #    and then call the add_item function.
        # 2. If the choice is '2', call the view_inventory function.
        # 3. If the choice is '3', prompt the user to enter an item name and new quantity,
        #    and then call the update_item function.
        # 4. If the choice is '4', break the loop to exit the program.
        # 5. For any other input, display an error message.
        pass

def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

if choice == "1":
    item = input("Enter Item:")
    quantity  = ini(input("input"))
    add_item(item, quantity)
elif choice == "2":
    view_inventory()
elif choice == "3":
    item = input("Enter item:")
    quantity = ini(input("Enter quantity:"))


    





# 5 Entry point of the program
if __name__ == "__main__":
    manage_inventory()



add_item(1, "商品4", 19.99, 9)
add_item(2, "商品5", 21.99, 7)