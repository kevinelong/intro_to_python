input_file = open("file_write.txt", "r")
line_list = input_file.readlines()
for line in line_list:
    print(line)