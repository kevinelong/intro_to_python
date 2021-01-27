# STore
# cart
# NOUNS/CLASSES: Categories e.g Electronics, Products: e.g. Television,
# AJECTIVES/ PROPERTIES: Product has: name, desc, price, stars, maker/brand
# VERBS:METHOD/FUNCTION: show __str__, compare

# CartItem product.price, quantity, VERB: subtotal(), show_checkout __str__



class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}"


class Category:
    def __init__(self, name):
        self.name = name
        self.products = []  # HAS A ... contains

    def __str__(self):
        lines = []
        for p in self.products:
            lines.append("\t" + str(p))
        return "\n" + self.name.capitalize() + "\n" + "\n".join(lines)


class Store:
    def __init__(self, name):
        self.name = name
        self.categories = []

    def __str__(self):
        lines = []
        for c in self.categories:
            lines.append("\t" + str(c))
        return self.name + "\n" + "\n".join(lines)


office = Category("office")

office.products = [
    Product("paper", 100),
    Product("glue", 2.50)
]

s = Store("Bam-azon")
s.categories = [
    office
]
print(s)

# SHOW METHODS OF STRING
# print(dir(str))
