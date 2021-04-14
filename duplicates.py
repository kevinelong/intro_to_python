# REMOVE DUPLICATES
# More ways can be seen here: https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/

def remove_duplicates_from_list(data):
    unique_values = []
    for item in data:
        if item not in unique_values:
            unique_values.append(item)
    return unique_values

data = ["apple", "orange", "apple", "pear", "orange"]
print(remove_duplicates_from_list(data))