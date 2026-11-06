import json
from physicalproduct import PhysicalProduct
from digitalproduct import DigitalProduct
from inventory import Inventory

class FileHandling:
    def __init__(self, filename="inventory.json"): 
        self.__filename = filename

    def load_inventory(self):
        inventory = Inventory()
        try:
            with open(self.__filename, "r") as file:
                data = json.load(file)
                for item in data:
                    if item["type"] == "physical":
                        product = PhysicalProduct(item["product_id"], item["name"], item["price"], item["stock"], item["weight"])
                        inventory.add_product(product)
                    elif item["type"] == "digital":
                        product = DigitalProduct(item["product_id"], item["name"], item["price"], item["stock"], item["download_size"])
                        inventory.add_product(product)
                print(f"{self.__filename} loaded")
            return inventory
        except FileNotFoundError:
            print(f"{self.__filename} file not found. Creating new {self.__filename} file.")
            with open(self.__filename, "w") as file:
                json.dump([], file)
            return inventory

    def save_inventory(self, inventory):
        print("\nSaving Inventory...")
        data = [p.return_product_dict() for p in inventory.get_products()]
        with open(self.__filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Inventory saved to {self.__filename}\n")