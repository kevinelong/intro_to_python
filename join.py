text_list = [
    "Larry",
    "Moe",
    "Curly"
]
print(text_list)
glue = " : "
together = glue.join(text_list)
print(together)

# ---

raw_text = "apple orange pear"
print(raw_text)
separator = " "
fruit_list = raw_text.split(separator)
print(fruit_list)

line_glue = "\n"  # new line
document = line_glue.join(fruit_list)

print(document)
