class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class InvoiceItem:
    def __init__(self, product, quantity=1):
        self.product = product
        self.quantity = quantity

    def extended_price(self):
        return self.quantity * self.product.price


class Cart:
    def __init__(self):
        self.item_list = []

    def total(self):
        prices = []
        for p in self.item_list:
            prices.append(p.extended_price())
        return sum(prices)

    def display(self):
        for item in self.item_list:
            print(item.quantity, item.product.name, item.product.price, item.extended_price())
        print(f"TOTAL: {self.total()}")

    def add_product(self, product, quantity=1):
        self.item_list.append(InvoiceItem(product, quantity))


products = [
    Product("rocks", 111.00),
    Product("paper", 222.00),
    Product("scissors", 333.00)
]

c = Cart()
c.add_product(products[1], 2)
c.add_product(products[2], 3)
c.display()
