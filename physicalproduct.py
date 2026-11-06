from product import Product
from canbeshipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__ (self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight:.2f} kg")

    def get_fulfilment_info(self):
        print("This product requires physical shipping.")
        print(f"Shipping will cost ${self.calculate_shipping_cost():.2f}")

    def return_product_dict(self):
        data = super().return_product_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data

    def calculate_shipping_cost(self):
        shipping_cost = self.__weight*2.5
        return shipping_cost