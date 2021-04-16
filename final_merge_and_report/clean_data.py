# data = [['1', '2020-12-30', ' kevin@example.com', ' mary@example.com', 'Demo', 'Now is the time...\n', 'mail_source1.csv'], ['2', '2020-12-30', ' kevin@example.com', ' mary@example.com', 'Demo', 'Now is the time...\n', 'mail_source1.csv'], ['3', '2020-12-29', ' bob@example.com', ' mary@example.com', 'Demo', 'Now is the time...\n', 'mail_source1.csv'], ['4', '2020-12-29', ' bob@example.com', ' mary@example.com', 'Demo', 'Now is the time...\n', 'mail_source1.csv'], ['5', '2020-12-29', ' info@example.com', ' mary@example.com', 'Demo', 'Now is the time...\n', 'mail_source1.csv'], ['1', '2020-12-30', ' kevin@example.com', ' joe@example.com', 'Demo', 'Now is the time...\n', 'mail_source2.csv'], ['2', '2020-12-30', ' kevin@example.com', ' joe@example.com', 'Demo', 'Now is the time...\n', 'mail_source2.csv'], ['3', '2020-12-28', ' bob@example.com', ' joe@example.com', 'Demo', 'Now is the time...\n', 'mail_source2.csv'], ['4', '2020-12-28', ' sales@example.com', ' joe@example.com', 'Demo', 'Now is the time...\n', 'mail_source2.csv'], ['5', '2020-12-29', ' bob@example.com', ' joe@example.com', 'Demo', 'Now is the time...\n', 'mail_source2.csv'], ['1', '2020-12-30', ' kevin@example.com', ' alice@example.com', 'Demo', 'Now is the time...', 'data'], ['2', '2020-12-30', ' kevin@example.com', ' alice@example.com', 'Demo', 'Now is the time...', 'data'], ['3', '2020-12-29', ' bob@example.com', ' alice@example.com', 'Demo', 'Now is the time...', 'data'], ['4', '2020-12-29', ' bob@example.com', ' alice@example.com', 'Demo', 'Now is the time...', 'data'], ['5', '2020-12-29', ' info@example.com', ' alice@example.com', 'Demo', 'Now is the time...', 'data']]
#
# # CLEAN USING DUPLICATES
# clean_output = []
# for row in data:
#     clean_row = []
#     for column in row:
#         clean_row.append(column.strip())
#     clean_output.append(clean_row)
#
# print(clean_output)


# CLEAN IN PLACE
def clean_matrix(data):
    for row_index in range(len(data)):
        for column_index in range(len(data[row_index])):
            data[row_index][column_index] = data[row_index][column_index].strip()
    return data

# print(clean_matrix(data))
