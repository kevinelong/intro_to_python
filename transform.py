# this is what we start with
data = [
    {
        "id": "123",
        "name": "Kevin",
        "age": "53"
    },
    {
        "id": "456",
        "name": "Nina",
        "age": "44"
    }
]


def transform(data):
    output = {}
    # TODO loop through items in data and add each to the output dictionary
    for item in data:
        id_value = item["id"]
        # del item["id"]  # optionally we can also delete the old id
        output[id_value] = item  # use the id as the key and add the old inner dict to the new outer output dict
    return output


result = transform(data)

print(result)
print(result["456"]["name"])

import json
print(json.dumps(result, indent=4))

# This is what we want
# desired = {
#     "123" : {
#         "id" : "123",
#         "name" : "Kevin",
#         "age" : "53"
#     },
#     "456" : {
#         "id" : "456",
#         "name" : "Nina",
#         "age" : "44"
#     }
# }
# # so we can look things up directly by id
# print(desired["456"]["name"])