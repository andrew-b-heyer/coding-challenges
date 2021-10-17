# This class is responsible for the representation of the stock levels of a store
from copy import copy
from datetime import datetime


class Inventory:
    def __init__(self, name=None):
        self.name = name

        # The inventory is a dictionary type where key's are the SKU, and the value is of Product type.
        # self.inventory_* = {"sku" : [product, product, .. product], "sku" : [...]}
        self.inventory_products = {}

        # keeps a mapping of SKU and the fields of a product to help
        self.inventory_record = {}

        # products who we forecasted were to be sold but we were out of stock
        self.inventory_lost_sales = {}

        # products who have been expired
        self.inventory_expired = {}

    # Because we have 3 inventories with the same data structure but used to represent different
    # use cases, we have an inventory helper
    @staticmethod
    def inventory_helper_add_product(product, inventory):
        inventory = inventory
        sku = product.get_sku()
        name = product.name
        # If the product SKU exists within our inventory
        if inventory.get(sku):
            # Then the name must be the same in order to be added
            current_sku_name = inventory.get(sku)[0].name
            if name == current_sku_name:
                inventory.get(sku).append(product)
            else:
                # print("Cannot add product, the sku are the same but the names differ")
                return
        else:
            inventory[sku] = [product]

    def create_product_record(self):
        for sku in self.get_sku_list():
            first_product = self.inventory_products.get(sku)[0]
            new_product = first_product.new_product()
            self.inventory_record[sku] = new_product

    def add_product_sku(self, sku):
        product = self.inventory_record[sku].new_product()
        self.inventory_helper_add_product(product, self.inventory_products)

    def add_product(self, product):
        self.inventory_helper_add_product(product, self.inventory_products)

    def add_lost_sale(self, sku):
        if sku in self.get_lost_sales_inventory():
            self.inventory_lost_sales[sku] += 1

        else:
            self.inventory_lost_sales[sku] =1

    def add_expired_product(self, product):
        self.inventory_helper_add_product(product, self.inventory_expired)

    # The same as remove product except allows us to remove with a SKU
    def remove_sku(self, sku):
        sku = sku
        if self.get_inventory().get(sku) is None:
            # print("Product with SKU:" + str(sku) + " does not exist")
            return

        else:
            if self.get_stock(sku) == 0:
                # print("Product has an inventory of 0, we lost a sale")
                self.add_lost_sale(sku)
            else:
                self.get_inventory().get(sku).pop(0)

    def remove_product(self, product):
        sku = product.sku
        if self.get_inventory().get(sku) is None:
            # print("Product with SKU:" + str(sku) + " does not exist")
            return

        else:
            if self.get_stock(sku) == 0:
                # print("Product has an inventory of 0, we lost a sale")
                self.add_lost_sale(product)
            else:
                self.get_inventory().get(sku).pop(0)

    # Cleans out the inventory for any products that have expired
    def clean_inventory(self, date=None):
        inventory = self.get_inventory()
        today = date
        if today is None:
            today = datetime.today()

        for sku in inventory:
            product_list = self.get_product_list(sku)
            product_list_length = len(product_list)

            print("product_list: " + str(product_list))
            print("length: " + str(product_list_length))
            for i in range(0, product_list_length):
                product = product_list[0]

                if product.is_expired(today):
                    self.remove_product(product)
                    self.add_expired_product(product)
                else:
                    break

    # Return stock of given SKU
    def get_stock(self, sku):
        return len(self.get_inventory().get(sku))

    def get_total_stock(self):
        total = 0
        inventory = self.get_inventory()
        for key in inventory:
            total += self.get_stock(key)
        return total

    # Return lost sales stock of given SKU
    def get_lost_sales_count(self, sku):
        return len(self.get_lost_sales_inventory().get(sku))

    def get_expired_product_count(self, sku):
        return len(self.get_expired_product_inventory().get(sku))

    # Return list of products of given SKU
    def get_product_list(self, sku):
        return self.inventory_products.get(sku)

    def get_sku_list(self):
        skus = []
        for sku in self.get_inventory():
            skus.append(sku)
        return skus

    # Return entire inventory data structure
    def get_inventory(self):
        return self.inventory_products

    # Return entire lost sales inventory data structure
    def get_lost_sales_inventory(self):
        return self.inventory_lost_sales

    def get_expired_product_inventory(self):
        return self.inventory_expired

    def __repr__(self):
        inventory_string = ""
        inventory = self.get_inventory()
        for sku in inventory:
            length = len(inventory[sku])

            inventory_string += str(sku) + " " + str(length) + "\n\n"
        return inventory_string
