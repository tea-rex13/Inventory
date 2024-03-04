from tabulate import tabulate

class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"

shoe_list = []
def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # Skip the header line
            for line in file:
                data = line.strip().split(",")
                country, code, product, cost, quantity = data
                cost = int(cost)
                quantity = int(quantity)
                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)
        print("Shoe data read successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error: {e}")

def capture_shoes():
        country = input("Enter country: ")
        code = input("Enter code: ")
        product = input("Enter product: ")
        cost = int(input("Enter cost whole numbers only: "))
        quantity = int(input("Enter quantity: "))
        shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe)
        print("Shoe captured successfully.")

def view_all():
    print("Inside view_all() function.")
    if shoe_list:
        print("Shoe list is not empty.")
        headers = ["Country", "Code", "Product", "Cost", "Quantity"]
        data = [[shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity] for shoe in shoe_list]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    else:
        print("No shoes available.")
def re_stock():
    if not shoe_list:
        print("No shoes available for restocking.")
        return
    min_quantity_shoe = min(shoe_list, key=lambda x: x.quantity)
    print(f"Lowest quantity shoe: {min_quantity_shoe}")
    restock_quantity = int(input("Enter quantity to restock: "))
    min_quantity_shoe.quantity += restock_quantity
    print("Restocking successful.")

def search_shoe():
    code = input("Enter shoe code to search: ")
    found_shoe = None
    for shoe in shoe_list:
        if shoe.code == code:
            found_shoe = shoe
            break
    if found_shoe:
        print(found_shoe)
    else:
        print("Shoe not found.")

def value_per_item():
    if shoe_list:
        print("Value per item:")
        for shoe in shoe_list:
            value = shoe.cost * shoe.quantity
            print(f"{shoe.product}: {value}")
    else:
        print("No shoes available.")

def sale_items():
    if shoe_list:
        max_quantity_shoe = max(shoe_list, key=lambda x: x.quantity)
        print(f"Sale item: {max_quantity_shoe}")
    else:
        print("No shoes available.")

def remove_stock():
    if not shoe_list:
        print("No shoes available.")
        return
    
    code = input("Enter the code of the shoe to remove stock: ")
    found = False

    for shoe in shoe_list:
        if shoe.code == code:
            found = True
            quantity_to_remove = int(input(f"Enter quantity to remove for {shoe.product}: "))
            if quantity_to_remove > shoe.quantity:
                print("Error: Quantity to remove exceeds available quantity.")
            else:
                shoe.quantity -= quantity_to_remove
                print(f"Successfully removed {quantity_to_remove} units of {shoe.product} from stock.")
            break

    if not found:
        print("Shoe not found.")

main_menu = True
while True:
    print("\nShoe Inventory")
    print("--------------")

    options = [
        ["1", "Read in shoes data"],
        ["2", "Capture a new shoe"],
        ["3", "View all shoes"],
        ["4", "Re-stock a shoe"],
        ["5", "Search for a shoe"],
        ["6", "Value of stock"],
        ["7", "Sale items"],
        ["8", "Remove Stock"],
        ["9", "Quit"]
    ]

    print(tabulate(options, headers=["Option", "Description"]))

    choice = input("Enter your choice: ")

    if choice == "1":
        read_shoes_data()
    elif choice == "2":
        capture_shoes()
    elif choice == "3":
        view_all()
    elif choice == "4":
        re_stock()
    elif choice == "5":
        search_shoe()
    elif choice == "6":
        value_per_item()
    elif choice == "7":
        sale_items()
    elif choice == "8":
        remove_stock()
    elif choice == "9":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")