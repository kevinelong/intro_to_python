source_file = open("csv_migrate_source.csv","r")
source = list(source_file.readlines())

column_source_file = open("csv_migrate_target.csv","r")
ouput_fields = column_source_file.readlines()[0].split(",") #only the first line
column_source_file.close()

target_file = open("csv_migrate_target.csv","a")

columns_to_migrate = ["a", "c"]

input_fields = source[0]

for item in source[1:]: #skip first line
    output = []
    for column in ouput_fields:
        if column in columns_to_migrate:
            index = input_fields.index(column)
            output.append(item[index])
        else:
            output.append("TBD")
    target_file.write(",".join(output) + '\n')
target_file.close()

# source = [
#     ["a","b","c","d"],
#     [123,456,345,787],
#     [222,456,345,787],
#     [333,456,345,787],
# ]

# target = [
#     ["z","a","c","d"],
# ]