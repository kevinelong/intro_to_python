"""
NOUNS people, places, things -> classes/objects
products
categories

VERBS - Actions -> method (functions)
details
get_tile
get_products
get_categories

ADJECTIVE - properties - attributes - (variables)
name
desc
price
image_url
"""


class Product:
    def __init__(self, name, desc, price, image_url):
        self.name = name
        self.desc = desc
        self.price = price
        self.image_url = image_url

    def __str__(self):
        return f"""
<div style="height:175px;display:inline-block;margin:1em">
<img src="{self.image_url}" style="width:150px;"><br>
{self.name}<br>
{self.price}<br>
{self.desc}
</div>
"""


class Category:
    def __init__(self, name, product_list):
        self.name = name
        self.product_list = product_list

    def __str__(self):
        product_text = []
        for p in self.product_list:
            product_text.append(str(p))
        return f"<h3>{self.name}:</h3>" + " ".join(product_text)


class Store:
    def __init__(self, name):
        self.name = name
        self.categories = [
            Category("Leather Goods", [
                Product("Belt", "46inch black and silver", 45.00,
                        "https://i.etsystatic.com/19311499/r/il/b4be61/1839533908/il_794xN.1839533908_lgk6.jpg"),
                Product("Wallet", "black bifold", 35.00,
                        "https://i.etsystatic.com/19311499/r/il/b4be61/1839533908/il_794xN.1839533908_lgk6.jpg"),
            ]),
            Category("Toy", [
                Product("Slime", "yellow spkly butter slime", 5.00,
                        "https://i.etsystatic.com/15242951/r/il/f20768/2308055638/il_794xN.2308055638_dhud.jpg"),
                Product("Juggling balls", "set of three in random colors", 55.00,
                        "https://i.etsystatic.com/15242951/r/il/f20768/2308055638/il_794xN.2308055638_dhud.jpg"),
            ]),
        ]

    def __str__(self):
        text = []
        for c in self.categories:
            text.append(str(c))
        return f"<body style=\"font-family:sans-serif\"><h1>{self.name}:</h1>" + "<br>".join(text) + "</body>"


open("shop.html", "w").write(str(Store("Wild Bill's Shop-o-roma")))
