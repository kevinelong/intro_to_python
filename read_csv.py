
file_name = "products.csv"
input_file = open(file_name, "r")

line_list = input_file.readlines()

ID_FIELD = 0
NAME_FIELD = 1
menu = {}
index = 0

for line in line_list:
    if index > 0:
        parts = line.split(",")
        menu[parts[ID_FIELD]] = parts
        # print(parts[NAME_FIELD])
    index += 1


import json
print(json.dumps(menu, indent=4))
