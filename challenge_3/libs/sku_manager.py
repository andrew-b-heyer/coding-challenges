# Responsible for the generation of SKU's as well as checking for manually entered SKU's
import logging
import random

from models.sku import SKU

# These variables were taken from the coding challenge with Luke
SKU_LENGTH = 12
SKU_TOTAL = 100

log = logging.getLogger(__name__)


def check_sku(sku=None):
    # Initial check if SKU is of none type
    if sku is None:
        raise ValueError("SKU must not be of None type")

    if len(sku) != SKU_LENGTH:
        raise ValueError("SKU length must be exactly: " + str(SKU_LENGTH))

    odd_count = 0
    even_count = 0

    for i in range(0, SKU_LENGTH):
        if i % 2 == 0:
            odd_count += sku[i]
        if i % 2 == 1:
            even_count += sku[i]

    sku_count = odd_count*3 + even_count

    # print("Evaluating SKU "
    #       "oddCount: " + str(odd_count) +
    #       "even count: " + str(even_count) +
    #       "total count: " + str(sku_count))

    if sku_count < SKU_TOTAL:
        return False

    if sku_count == SKU_TOTAL:
        return True


# This function attempts at creating a properly formatted SKU
# TODO not the most space efficient method of comparing a sku after creating
# an entire object. If performance is effected may be best to refactor this.
def generate_sku():
    sku = SKU(str(random.randint(100000000000, 999999999999)))
    while not check_sku(sku):
        sku = SKU(str(random.randint(100000000000, 999999999999)))
    return sku


def generate_unique_sku(inventory):
    sku = generate_sku()
    current_sku = inventory.get_inventory().keys()
    # Keep generating sku until you generate one that does not exist within the inventory
    # print(sku)
    # print(current_sku)

    while sku.sku in current_sku:
        sku = generate_sku()
    return sku
