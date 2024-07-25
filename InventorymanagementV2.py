'''
//pseudocode
class InventorySystem:
    initialize:
        items dictionary

    additem method:
        Add items and their quantity as objects to the dictionary

    restock method:
        Restocks items based on specific item name and inputted quantity

    deduct method:
        Deducts items based on specific item name and inputted quantity

    viewinventory method:
        Print your inventory with all items

main function:
    define menu as string
    menu:

        Inventory Management System
        ----------------------------
        1. Add item
        2. Restock item
        3. Deduct item
        4. View inventory
        5. Exit
        Choose number:

    display menu

    loop until user chooses to exit:
        get users choice

        if users choice = 1:
            use additem function

        if users choice = 2:
            use restock function

        if users choice = 3:
            use deduct function

        if users choice = 4:
            use viewinventory function

        if users choice = 5:
            leave program


'''

class InventorySystem:
    def __init__(self):
        self.items = {}


    def additem(self):
        item = input("Input the item name you want to add: ")
        quantity = int(input("Input the item quantity: "))
        if not item in self.items.keys():
            self.items[item] = quantity
            print(f"Item {item} with quantity of {quantity} successfully created!")
        else:
            print("This item already exists!")

    def restock(self):
        item = input("Input the item name you want to restock: ")
        quantity = int(input("Input the item quantity: "))
        if not item in self.items.keys():
            print("This item does not exists!")
        elif quantity > 0:
            self.items[item] = self.items[item] + quantity
            print(f"Successfully added {quantity} items, You have {self.items[item]} {item}'s in your stock  ")
        else:
            print("Please enter the positive integer!")
    def deduct(self):
        item = input("Input the item name you want to deduct: ")
        quantity = int(input("Input the item quantity: "))
        if not item in self.items.keys():
            print("This item does not exists!")
        elif quantity > 0:
            self.items[item] = self.items[item] - quantity
            print(f"Successfully substracted {quantity} items, You have {self.items[item]} {item}'s in your stock  ")
        else:
            print("Please enter the positive integer!")

    def viewinventory(self):
        print("YOUR INVENTORY:")
        for item,quantity in self.items.items():
            print(f"Item name: {item}, Quantity: {quantity}")

def main():
    shop = InventorySystem()

    menu = '''
Inventory Management System
----------------------------
1. Add item
2. Restock item
3. Deduct item
4. View inventory
5. Exit
Choose number: '''
    while True:
        try:
            choice = int(input(menu))
            if choice == 1:
                shop.additem()
            elif choice == 2:
                shop.restock()
            elif choice == 3:
                shop.deduct()
            elif choice == 4:
                shop.viewinventory()
            elif choice == 5:
                print("Successfully exited!")
                break
        except ValueError:
            print("Please enter the number!")



main()