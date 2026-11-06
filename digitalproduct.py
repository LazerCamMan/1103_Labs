from product import Product

class DigitalProduct(Product):
    def __init__ (self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.__download_size:.2f} MB")

    def get_fulfilment_info(self):
        print("This product needs to be downloaded online")

    def return_product_dict(self):
        data = super().return_product_dict()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data