def write_list_to_file(text_list, file_name):
    output_file = open(file_name, "w")
    output_data = "\n".join(text_list)
    output_file.write(output_data)
    output_file.close()


def read_list_from_file(file_name):
    input_file = open(file_name, "r")
    line_list = input_file.readlines()
    output_word_list = []
    input_file.close()

    for w in line_list:
        output_word_list.append(w.strip())

    return output_word_list


# word_list = ["Larry", "Moe", "Curly"]
#
# write_list_to_file(word_list, "data.txt")
# print(word_list)

result_word_list = read_list_from_file("data.txt")

print(result_word_list)

# assert word_list == result_word_list
