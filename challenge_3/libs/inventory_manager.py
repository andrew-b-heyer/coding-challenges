from libs.sku_manager import generate_unique_sku
from models.product import Product

from datetime import datetime

from faker import Faker


def generate_products(inventory, category, set_count, count, shelf_life, cost, price):
    fake = Faker()
    names = [fake.unique.first_name() for i in range(set_count)]
    today = datetime.today()
    for i in range(0, set_count):
        sku = generate_unique_sku(inventory)
        for n in range(0, count):
            # print("attempting to creater prod " + str(i))
            product = Product(sku, names[i], cost, price, category, shelf_life, today)
            inventory.add_product(product)

