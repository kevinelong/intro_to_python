
output_file = open("output1.txt", "w")  # w write, a append, r for read

output_file.write("\neven more stuff to write\n")

output_file.close()

input_file = open("output1.txt", "r")

text_list = input_file.readlines()

print(text_list)

for line in text_list:
    print(line.strip())
