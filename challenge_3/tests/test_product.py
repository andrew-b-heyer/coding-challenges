import unittest

from datetime import datetime
from datetime import timedelta

from libs.product_categories import product_category
from models.product import Product


class TestProduct(unittest.TestCase):
    # Normally we shouldn't manually create SKU's and allow the skuManager to do this so that we have properly formatted
    # SKU
    def test_create_product(self):
        self.today = datetime.today()

        prod = Product(sku="1111", name="taco", cost=1.0, price=2.0, shelf_life=1, created=self.today,
                       category=product_category.LUNCH)

        self.assertEqual(prod.sku, "1111")
        self.assertEqual(prod.name, "taco")
        self.assertEqual(prod.cost, 1.0)
        self.assertEqual(prod.price, 2.0)
        self.assertEqual(prod.shelf_life, 1)
        self.assertEqual(prod.category, product_category.LUNCH)

    # Products as I use them are allowed to have all the same properties except for SKU. SKU must be unique.
    def test_duplicate_product(self):
        self.today = datetime.today()

        prod1 = Product(sku="1111", name="taco", cost=1.0, price=2.0, shelf_life=1, created=self.today,
                        category=product_category.LUNCH)
        prod2 = Product(sku="1111", name="taco", cost=1.0, price=2.0, shelf_life=1, created=self.today,
                        category=product_category.LUNCH)
        prod3 = Product(sku="2222", name="taco", cost=1.0, price=2.0, shelf_life=1, created=self.today,
                        category=product_category.LUNCH)

        self.assertEqual(prod1, prod2)
        self.assertNotEqual(prod1, prod3)

    # Test to be sure that our checks for expiration return correctly.
    def test_product_expiration_date(self):
        self.today = datetime.today()
        self.tomorrow = datetime.today()
        self.two_days_from_now = self.today + timedelta(days=2)

        prod1 = Product(sku="1111", name="taco", cost=1.0, price=2.0, shelf_life=1, created=self.today,
                        category=product_category.LUNCH)

        self.assertTrue(prod1.is_expired(self.two_days_from_now))
        self.assertFalse(prod1.is_expired(self.tomorrow))
