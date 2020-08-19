file_name = "products.csv"
output_file = open(file_name, "a")
line_list = [
    # ["ID", "NAME", "PRICE", "DESCRIPTION", "PHOTO_URL"],
    ["1003", "Meat Lovers", "39.99", "All the meats!!!", "http://www.example.com/photos/img_1001.png"],
    ["1004", "Veggie Delight", "39.99", "All the veg!!!", "http://www.example.com/photos/img_1002.png"],
]
for line in line_list:
    text = ",".join(line)
    output_file.write(text + "\n")
