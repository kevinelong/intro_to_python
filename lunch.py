class Sandwich:
    # CONSTRUCTOR
    def __init__(self, name, bread_type="", main_ingredient="", options_list=None):
        self.name = name
        self.bread_type: str = bread_type
        self.main_ingredient: str = main_ingredient
        self.options_list: [str] = options_list if options_list is not None else []

    def __str__(self):
        return f"{self.name} {self.main_ingredient} {self.options_list}"

    def cook(self):
        print("No cooking required")


class PBNJ(Sandwich):

    def __init__(self):
        super().__init__("Peanut butter and Jelly", "white", "Peanut Butter", ["Jelly"])


class Burger(Sandwich):

    def __init__(self):
        self.name = "Hamburger"
        self.bread_type: str = "Bun"
        self.main_ingredient: str = "Ground Beef"
        self.options_list: [str] = ["Ketchup"]

    def cook(self):
        print("Frying burger and toasting bun")


pbnj = PBNJ()

b = Burger()
lunch = [pbnj, b]

for item in lunch:
    print(item)
    item.cook()
