class Choice:
    def __init__(self, name, additional_price=0.0):
        self.name = name
        self.additional_price = additional_price

    def __str__(self):
        return f"{self.name} +${self.additional_price}"


class ChoiceSet:
    def __init__(self, name, choice_list):
        self.name = name
        self.choice_list: [Choice] = choice_list


class MenuItem:
    def __init__(self, name: str, price, choice_sets: [ChoiceSet] = None):
        self.name: str = name
        self.price = price
        self.choice_sets = choice_sets if choice_sets is not None else []


class Category:
    # CONSTRUCTOR CALLED AUTOMTICLLY WHEN CREATE AN INSTANCE e.g Category("drinks")
    def __init__(self, name: str, menu_items: [MenuItem] = None):
        self.name: str = name
        self.menu_items = menu_items if menu_items is not None else []

    def add_menu_item(self, menu_item):
        self.menu_items.append(menu_item)


class Menu:
    def __init__(self):
        self.category_list = []

    def add_category(self, category: Category):
        self.category_list.append(category)


class Customer:
    def __init__(self, name, phone, address):
        self.name: str = name
        self.phone: str = phone
        self.address: str = address
        self.licence_plate: str = ""
        self.car_make: str = ""
        self.car_model: str = ""


class LineItem:
    def __init__(self, menu_item: MenuItem, quantity=1, choices: [Choice] = None):
        self.menu_item = menu_item
        self.quantity = quantity
        self.choices: [Choice] = [] if choices is None else choices

    def subtotal(self):
        return self.quantity * self.menu_item.price

    def __str__(self):
        return f"{self.quantity} {self.menu_item.name} @{self.menu_item.price}={self.subtotal()}"


class Order:
    def __init__(self):
        self.customer: Customer = Customer("", "", "")
        self.item_list: [LineItem] = []

    def total(self):
        subtotal = 0
        for item in self.item_list:
            subtotal += item.subtotal()
            for c in item.choices:
                subtotal += c.additional_price
        return subtotal


# TESTS
if __name__ == "__main__":

    drinks = Category("Drinks")

    drinks.add_menu_item(MenuItem("Cola", 3.33))
    drinks.add_menu_item(MenuItem("Seltzer", 2.22))

    pizza = Category("Pizza")

    pizza.add_menu_item(MenuItem("Meat Lovers", 33.33))
    pizza.add_menu_item(MenuItem("Veggie Delight", 22.22))

    pizza.add_menu_item(MenuItem("custom_pizza", 44.44, [
        ChoiceSet("crust", [
            Choice("Regular"),
            Choice("Thin"),
            Choice("Deep", 5.00),
        ]),
        ChoiceSet("cheese", [
            Choice("Regular"),
            Choice("Mozzarella"),
            Choice("Vegan Cheese", 7.00),
        ])

    ]))

    menu = Menu()
    menu.add_category(pizza)

    order = Order()
    selection = menu.category_list[0].menu_items[0]
    order.item_list.append(LineItem(selection, quantity=2))

    custom_selection = menu.category_list[0].menu_items[2]
    order.item_list.append(LineItem(custom_selection, quantity=1, choices=[
        custom_selection.choice_sets[0].choice_list[2],  # crust - deep
        custom_selection.choice_sets[1].choice_list[2]
    ]))

    for item in order.item_list:
        print(item)
        for choice in item.choices:
            print(f"\t{choice}")
    print(f"TOTAL: {order.total():.2f}")
