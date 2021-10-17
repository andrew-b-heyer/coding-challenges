from libs.product_categories import product_category
from libs.inventory_manager import generate_products
from libs.sales_simulator import simulate_day_of_sales, make_smart_order

from models.inventory import Inventory

import pandas as pd
import matplotlib.pyplot as plt


def main():

    inventory = Inventory("Whole Food")

    generate_products(inventory=inventory, category=product_category.LUNCH, set_count=5,
                      count=200, shelf_life=7, cost=1.0, price=2.0)

    generate_products(inventory=inventory, category=product_category.BREAKFAST, set_count=5,
                      count=200, shelf_life=7, cost=1.0, price=2.0)

    generate_products(inventory=inventory, category=product_category.DINNER, set_count=5,
                      count=200, shelf_life=7, cost=1.0, price=2.0)

    inventory.create_product_record()


    # initialize the stock data data structure which is used for the dataframe
    stock_data = {}
    skus = inventory.get_sku_list()

    for sku in skus:
        stock_data[sku] = [inventory.get_stock(sku)]

    for i in range(0, 50):
        simulate_day_of_sales(inventory, i)

        for sku in skus:
            stock_data.get(sku).append(inventory.get_stock(sku))

        if i%10 == 0:
            make_smart_order(inventory)

    df = pd.DataFrame(stock_data)

    for sku in skus:
        plt.plot(df[sku])
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
