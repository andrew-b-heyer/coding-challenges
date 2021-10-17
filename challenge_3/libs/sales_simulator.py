import random

# The higher the number, the more likelihood of more products being purchased, perhaps can be the economy
PURCHASE_POWER_FACTOR = 1.20

BREAKFAST_FACTOR = 1.0
LUNCH_FACTOR = 1.0
DINNER_FACTOR = 1.0

SHELF_MAX = 200
MINIMUM_STOCK = 100

def simulate_day_of_sales(inventory, seed):
    # generate a random number of sales

    random.seed(seed)
    sales = []
    skus = inventory.get_sku_list()
    unique_product_count = len(skus)

    for i in range(0, unique_product_count):
        sales.append(random.randint(0, 10))

    for i in range(0, unique_product_count):
        sku = skus[i]
        sale_count = sales[i]
        for n in range(0, sale_count):
            inventory.remove_sku(sku)


def make_smart_order(inventory):
    # create a purchase order depending on the current stock levels -

    skus = inventory.get_sku_list()

    for sku in skus:
        sku_stock = inventory.get_stock(sku)
        replenish_stock = SHELF_MAX - sku_stock

        if sku_stock < MINIMUM_STOCK:

            for i in range(0, replenish_stock):
                inventory.add_product_sku(sku)


