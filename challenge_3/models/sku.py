# Simple SKU class to store the representation of a sku in two differenet formats
# this is useful depending on what operation you want to do on the SKU.
# For example, when doing comparisons the string representation is simpler.
# For doing SKU analysis a list representation gives access by index. No need
# for substrings, or slices to get the values we want.

class SKU:
    def __init__(self, sku):
        self.sku = sku
        self.skuList = [char for char in sku]

    def __getitem__(self, item):
        return int(self.skuList[item])

    def __eq__(self, other_sku):
        if self.sku == other_sku.sku:
            return True
        return False

    def __len__(self):
        return len(self.sku)
