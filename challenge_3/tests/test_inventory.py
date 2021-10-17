import unittest


from datetime import datetime, date
from datetime import timedelta

from models.inventory import Inventory
from models.product import Product

from libs.product_categories import product_category


class TestInventory(unittest.TestCase):
    def test_add_products(self):
        self.inventory = Inventory("WholeFoods")
        self.today = datetime.now()

        # Ensure that we can add a single product
        self.prod = Product(sku="1111", name="taco", cost=1.0, price=2.0, shelf_life=1, created=self.today,
                            category=product_category.LUNCH)
        self.inventory.add_product(self.prod)
        self.assertEqual(self.inventory.get_inventory().get("1111")[0], self.prod)

        # Ensure that we can add another product of the same SKU and seeing an increase in stock
        self.prod1 = Product(sku="1111", name="taco", cost=1.0, price=2.0, shelf_life=1, created=self.today,
                             category=product_category.LUNCH)
        self.inventory.add_product(self.prod1)
        self.assertEqual(self.inventory.get_stock("1111"), 2)

        # Ensure that adding a product with the same sku but different name returns and doesnt +1 the stock
        self.prod2 = Product(sku="1111", name="burger", cost=1.0, price=2.0, shelf_life=1, created=self.today,
                             category=product_category.LUNCH)
        self.inventory.add_product(self.prod2)
        self.assertEqual(self.inventory.get_stock("1111"), 2)

        # Ensure we can remove a product
        self.inventory.remove_product(self.prod1)
        self.assertEqual(self.inventory.get_stock("1111"), 1)

        # remove another product bringing us down to 0 stock
        self.inventory.remove_product(self.prod1)
        self.assertEqual(self.inventory.get_stock("1111"), 0)

    def test_lost_sales(self):
        self.inventory = Inventory("WholeFoods")
        self.today = datetime.now()

        # We must add a single product to initialize this SKU in our inventory before we can oversell
        self.prod = Product(sku="1111", name="taco", cost=1.0, price=2.0, shelf_life=1, created=self.today,
                            category=product_category.LUNCH)
        self.inventory.add_product(self.prod)
        self.assertEqual(self.inventory.get_stock("1111"), 1)

        self.inventory.remove_product(self.prod)
        self.assertEqual(self.inventory.get_stock("1111"), 0)

        self.inventory.remove_product(self.prod)
        self.assertEqual(self.inventory.get_stock("1111"), 0)
        self.assertEqual(self.inventory.get_lost_sales_count("1111"), 1)

        self.inventory.remove_product(self.prod)
        self.assertEqual(self.inventory.get_stock("1111"), 0)
        self.assertEqual(self.inventory.get_lost_sales_count("1111"), 2)

    def test_expired_product(self):
        self.inventory = Inventory("WholeFoods")
        self.shipment1 = date(2021, 9, 5)
        self.shipment2 = date(2021, 9, 10)

        self.shipment1_expired = date(2021, 9, 20)
        self.shipment2_expired = date(2021, 9, 25)

        # All shipment 1 products should expire
        self.prod1_shipment1 = Product(sku="1111", name="taco", cost=1.0, price=2.0, shelf_life=10,
                                       created=self.shipment1, category=product_category.LUNCH)
        self.prod2_shipment1 = Product(sku="2222", name="burger", cost=1.0, price=2.0, shelf_life=10,
                                       created=self.shipment1, category=product_category.LUNCH)

        self.prod1_shipment2 = Product(sku="1111", name="taco", cost=1.0, price=2.0, shelf_life=10,
                                       created=self.shipment2, category=product_category.LUNCH)
        self.prod2_shipment2 = Product(sku="2222", name="burger", cost=1.0, price=2.0, shelf_life=10,
                                       created=self.shipment2, category=product_category.LUNCH)

        self.inventory.add_product(self.prod1_shipment1)
        self.inventory.add_product(self.prod2_shipment1)
        self.inventory.add_product(self.prod1_shipment2)
        self.inventory.add_product(self.prod2_shipment2)
        self.assertEqual(self.inventory.get_total_stock(), 4)
        self.assertEqual(self.inventory.get_stock("1111"), 2)
        self.assertEqual(self.inventory.get_stock("2222"), 2)

        self.inventory.clean_inventory(self.shipment1_expired)
        self.assertEqual(self.inventory.get_expired_product_count("1111"), 1)
        self.assertEqual(self.inventory.get_expired_product_count("2222"), 1)
        self.assertEqual(self.inventory.get_total_stock(), 2)

        self.inventory.clean_inventory(self.shipment2_expired)
        self.assertEqual(self.inventory.get_expired_product_count("1111"), 2)
        self.assertEqual(self.inventory.get_expired_product_count("2222"), 2)

        self.assertEqual(self.inventory.get_total_stock(), 0)


if __name__ == '__main__':
    unittest.main()
