cart = [
    {
        "name": "pencil",
        "price": 0.25,
        "quantity": 144
    },
    {
        "name": "paper",
        "price": 0.05,
        "quantity": 10000
    },
]


class CartItem:
    def __init__(self, item_dict):
        self.name = item_dict["name"]
        self.price = item_dict["price"]
        self.quantity = item_dict["quantity"]

    def get_subtotal(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.quantity} {self.name} @${self.price} ${self.get_subtotal():.2f}"


class Cart:
    def __init__(self, cart_list):
        self.items = []
        for item_dict in cart_list:
            self.items.append(CartItem(item_dict))

    def display(self):
        print("CART ITEMS:")
        total = 0
        for item in self.items:
            print(f"\t{item}")
            total += item.get_subtotal()
        print(f"TOTAL: ${total:.2f}")

c = Cart(cart)
c.display()

# SOLVE
# 1. with script first,
# 2. then extra credit use a function on the cart,
# 3. extra extra credit use Product and Cart classes

"""
OUTPUT EXAMPLE:

CART ITEMS:
	144 pencil @$0.25 $36.00
	10000 paper @$0.05 $500.00
TOTAL: $536.00

"""