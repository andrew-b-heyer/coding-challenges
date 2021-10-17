from datetime import timedelta, datetime

class Product:
    def __init__(self, sku=None, name="", cost=0.0, price=0.0, category=None, shelf_life=None, created=None):
        self.sku = sku
        self.name = name
        self.cost = cost
        self.price = price
        self.category = category

        # We are using the datetime python module to help us calculate expired products.
        self.shelf_life = shelf_life
        self.creation_date = created
        self.expiration_date = created + timedelta(days=shelf_life)

        if sku is None:
            raise ValueError("SKU cannot be type None")

    # Simplify comparing product by delegating the comparison to the SKU class __eq__ class method
    def __eq__(self, other):
        if self.sku == other.sku:
            return True
        return False

    def __repr__(self):
        return self.name + " exp: " + str(self.expiration_date.date())

    def is_expired(self, current_date):
        if current_date > self.expiration_date:
            return True
        return False

    def get_sku(self):
        return self.sku.sku

    def new_product(self):
        new_date = datetime.today()
        product = Product(self.sku, self.name, self.cost, self.price, self.category, self.shelf_life, new_date)
        return product
