"""
Simple shopping cart systems allow the off-line administration of products and categories.
The shop is then generated as HTML files and graphics that can be uploaded to a webspace.
The systems do not use an online database.
[29] A high-end solution can be bought or rented as a stand-alone program
 or as an addition to an enterprise resource planning program.
 It is usually installed on the company's web server and may integrate into the existing supply chain so that
 ordering, payment, delivery, accounting and warehousing can be automated to a large extent.

NOUNS: Cart, Product, Catalog, Store

"""


class Product:
    def __init__(self, name, price, description="", category="NONE", sku=""):
        self.sku = sku
        self.name = name
        self.description = description
        self.category = category
        self.price = price
        self.on_hand = 144

    def __str__(self):
        price = self.price
        return f"{self.name} @ ${price:.2f}"


class Store:
    def __init__(self):
        self.inventory: [Product] = []

    def __str__(self):
        output = []
        for product in self.inventory:
            text = str(product) #convert to string
            output.append(text)
        return "\n".join(output)


class CartItem:
    def __init__(self, product, quantity=1):
        self.product = product
        self.quantity = quantity


# STATIC CLASS - NO INSTANCE
class OrderDeliveryMethod:
    USPS = 1
    PICKUP = 2
    COURIER = 3


class CartOrder:
    def __init__(self, delivery_method: OrderDeliveryMethod = OrderDeliveryMethod.USPS):
        self.items: [CartItem] = []
        self.delivery_method = delivery_method
        self.payment_amount = 0
        self.payment_method = ""
        self.payment_details = ""


# TEST
store = Store()
store.inventory.append(Product("pencil", 0.25))
store.inventory.append(Product("paper", 0.10))

print(store)
