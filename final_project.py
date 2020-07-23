"""
:40
Create a shopping cart class
that uses instance of product class
to add items to the cart
total the cart
display the cart
remove items from the cart
quantity of each item
prices from each item
catalog that is a list  of products

NOUNS/CLASS: Cart, LineItem, Display, Product, Catalog
ADJECTIVES/ATTRIBUTES: price, quantity
VERBS/METHODS: display, total()
"""


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"NAME: {self.name} - PRICE: {self.price}"


class Catalog:
    def __init__(self):
        self.product_list = []

    def add_product(self, product):
        self.product_list.append(product)


class LineItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def __str__(self):
        extension = self.quantity * self.product.price
        return f"{self.product.price} {self.product.name}  {self.quantity} {extension}"


class Cart:
    def __init__(self):
        self.line_items = []

    def add_item(self, product, quantity=1):
        self.line_items.append(LineItem(product, quantity))

    def total(self):
        t = 0
        for line in self.line_items:
            subtotal = line.quantity * line.product.price
            print(subtotal)
            t += subtotal
        return t

    def remove(self, line_item_index):
        self.line_items.remove(self.line_items[line_item_index])


class Display:
    def show(self, cart):
        text = "\nCART:\n"
        for item in cart.line_items:
            text += str(item) + "\n"
        text += f"\nTOTAL: {cart.total():.2f}"
        return text


p = Product(name="scissors", price=123.45)
print(p)

catalog = Catalog()
catalog.add_product(p)
catalog.add_product(Product(name="rock", price=2.34))
catalog.add_product(Product(name="paper", price=1.23))

scissors = catalog.product_list[0]
cart = Cart()
cart.add_item(scissors, quantity=12)
cart.add_item(catalog.product_list[1], quantity=6)
cart.add_item(catalog.product_list[2], quantity=3)

display = Display()
text_output = display.show(cart)
print(text_output)
assert (text_output.find("TOTAL") != -1)

cart.remove(line_item_index=1)
cart.line_items[0].quantity = 10
print(display.show(cart))

"""

C - Create
R - Read
U - Update
D - Delete

SQL
"""
