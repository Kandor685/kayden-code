class InventoryItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Name: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}"

class Inventory:
    def __init__(self):
        self.items = []
        self.initialize_items()  # Initialize with predefined items

    def initialize_items(self):
        # Predefined food items and prices
        food_items = {
            "Apple": 0.50,
            "Banana": 0.30,
            "Bread": 2.00,
            "Milk": 1.50,
            "Eggs": 2.50,
            "Chicken Breast": 5.00,
            "Rice": 1.00,
            "Pasta": 1.20,
            "Cheese": 3.00,
            "Tomato": 0.80
        }
        
        for name, price in food_items.items():
            self.add_item(name, price, quantity=10)  # Initialize each item with a quantity of 10

    def add_item(self, name, price, quantity):
        item = InventoryItem(name, price, quantity)
        self.items.append(item)
        print(f"Added: {item}")

    def remove_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                print(f"Removed: {item}")
                return
        print("Item not found.")

    def update_item(self, name, price=None, quantity=None):
        for item in self.items:
            if item.name == name:
                if price is not None:
                    item.price = price
                if quantity is not None:
                    item.quantity = quantity
                print(f"Updated: {item}")
                return
        print("Item not found.")

    def view_items(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            for item in self.items:
                print(item)

def main():
    inventory = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Item")
        print("4. View Items")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            inventory.add_item(name, price, quantity)

        elif choice == '2':
            name = input("Enter item name to remove: ")
            inventory.remove_item(name)

        elif choice == '3':
            name = input("Enter item name to update: ")
            price = input("Enter new price (leave blank to keep current): ")
            quantity = input("Enter new quantity (leave blank to keep current): ")
            price = float(price) if price else None
            quantity = int(quantity) if quantity else None
            inventory.update_item(name, price, quantity)

        elif choice == '4':
            inventory.view_items()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
