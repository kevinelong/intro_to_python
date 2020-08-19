class Product:
    def __init__(self, id, name, price, description):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
    def __repr__(self):
        return f"Product({self.id}, '{self.name}', {self.price}, '{self.description}')"
file_name = "products.csv"
input_file = open(file_name, "r")

line_list = input_file.readlines()
# FAKE READ FROM FILE
fakeline_list = [
    "ID,NAME,PRICE,DESCRIPTION,PHOTO_URL",
    "1001,Meat Lovers,29.99,All the meats!,http://www.example.com/photos/img_1001.png",
    "1002,Veggie Delight,29.99,All the veg!,http://www.example.com/photos/img_1002.png",
]
ID_FIELD = 0
NAME_FIELD = 1
menu = {}
index = 0
for line in line_list:
    if index > 0:
        # print(line)
        parts = line.split(",")
        # print(parts)
        # print(len(parts))
        # menu[parts[ID_FIELD]] = Product(parts[0], parts[1], parts[2], parts[3])  # [NAME_FIELD]
        menu[parts[ID_FIELD]] = parts
    index += 1
print(menu)

import json
print(json.dumps(menu, indent=4))