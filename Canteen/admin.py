import csv
class InventoryManager:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.inventory = self.load_inventory()

    def load_inventory(self):
        inventory = {}
        with open(self.csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                item_name = row['Item Name']
                quantity = int(row['Quantity'])
                price = float(row['Price'])
                inventory[item_name] = {'quantity': quantity, 'price': price}
        return inventory

    def save_inventory(self):
        with open(self.csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Item Name', 'Quantity', 'Price'])
            for item, details in self.inventory.items():
                writer.writerow([item, details['quantity'], details['price']])

    def display_inventory(self):
        print("Inventory:")
        for item, details in self.inventory.items():
            print(f"{item}: Quantity: {details['quantity']}, Price: {details['price']}")
    
    def get_item_names(self):
        return list(self.inventory.keys())

    def add_item(self):
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        self.inventory[item_name] = {'quantity': quantity, 'price': price}
        print(f"{quantity} {item_name}(s) added to inventory.")

    def update_quantity(self):
        l=list(self.inventory.keys())
        item = int(input("Enter item : "))
        item_name = l[item-1]
        if item_name in self.inventory:
            new_quantity = int(input("Enter new quantity: "))
            self.inventory[item_name]['quantity'] = new_quantity
            print(f"Quantity of {item_name} updated to {new_quantity}.")
        else:
            print("Item not found in inventory.")

    def update_price(self):
        item_name = input("Enter item name: ")
        if item_name in self.inventory:
            new_price = float(input("Enter new price: "))
            self.inventory[item_name]['price'] = new_price
            print(f"Price of {item_name} updated to {new_price}.")
        else:
            print("Item not found in inventory.")
def file():
    print("Admin Manager ")
    print("1. Edit Snacks")
    print("2. Edit Lunch")
    print("3. Edit Drinks")
    ch=int(input("Enter the options: "))
    if ch == 1:
        return "snack.csv"
    elif ch == 2:
        return "lunch.csv"
    elif ch == 3:
        return "drink.csv"
    else:
        print("Invalid choice. Please try again.")
    

def admin():
    csv_file = file()
    manager = InventoryManager(csv_file)
    manager.load_inventory()
    while True:
        print("\nMenu:")
        print("1. View Inventory")
        print("2. Add Item to Inventory")
        print("3. Update Item Quantity")
        print("4. Update Item Price")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            manager.display_inventory()
        elif choice == '2':
            manager.add_item()
        elif choice == '3':
            manager.update_quantity()
        elif choice == '4':
            manager.update_price()
        elif choice == '5':
            manager.save_inventory()
            print("Inventory saved. Exiting program.")
            create_home_page_widgets()
            break
        else:
            print("Invalid choice. Please try again.")
