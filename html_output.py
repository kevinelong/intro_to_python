data_list = ["123", "345", "234", "111"]

write_me = "<BR>\n".join(data_list)
output_file = open("html_output.html", "w")
output_file.write(write_me)
output_file.close()

#  ---

columns_list = ["AAA", "BBB", "CCC", "DDD"]

colors = ["red", "green", "blue", "black"]

output = "<table>"

for index in range(len(columns_list)):
    column_name = columns_list[index]
    value = data_list[index]
    color = colors[index]

    output += "<tr><td>"
    output += column_name
    output += "</td><td><div style=\"width:"
    output += value
    output += "px;height:1em;display:inline-block;background:"
    output += color
    output += "\"></div>("
    output += value
    output += ")</td></tr>"

output += "</table>"

output_file = open("html_output_bars.html", "w")
output_file.write(output)
output_file.close()


#  ---

def int_to_hex(i):
    h = hex(i)
    s = str(h)
    o = s.split("0x")[1]
    if len(o) < 2:
        o = "0" + o
    return o


# print(int_to_hex(128))

def rgb_int_list_to_hex_string(rgb_list):
    output = []
    for i in rgb_list:
        output.append(int_to_hex(i))
    return "".join(output)


color_output = []
limit = 256
step = 8
for r in range(0, limit, step):
    for g in range(0, limit, step):
        for b in range(0, limit, step):
            row = "<div style=\"height:1em;width:1em;display:inline-block;background:#"
            row += rgb_int_list_to_hex_string([r, g, b])
            row += "\"></div>"
            color_output.append(row)

output_file = open("html_output_colors.html", "w")
output_file.write("\n".join(color_output))
output_file.close()
