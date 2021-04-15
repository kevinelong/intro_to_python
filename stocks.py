#  list of dicts
stocks = [
    {
        "name": "TMUS",
        "closing": "200.00",
        "date": "2020-12-30",
    },
    {
        "name": "TMUS",
        "closing": "220.00",
        "date": "2020-12-31",
    },
    {
        "name": "MSFT",
        "closing": "100.00",
        "date": "2020-12-30",
    },
    {
        "name": "MSFT",
        "closing": "110.00",
        "date": "2020-12-31",
    }
]
# TODO CONVERT THE ABOVE TO THE BELOW
output_dict = {}  # Create empty dictionary to hold out output
for s in stocks:  # Loop through all the stocks in the list
    name = s["name"]

    if name not in output_dict:  # is key not in output dict? better create the key and assign empty list
        output_dict[name] = []  # Initialize new key in dict with empty list
    output_dict[name].append(s)

    # if name not in list(output_dict):  # is key not in output dict? better create the key and assign empty list
    #     output_dict[name] = [s]  # Initialize new key in dict with empty list
    #     # output_dict[name].append(s)
    # else:
    #     output_dict[name].append(s)
    
    del s["name"]
print(output_dict)

# PPRINT FOR PRETTY PRINTING
import pprint
pprint.PrettyPrinter(indent=4, depth=3, width=60).pprint(output_dict)

# or use json
import json
print(json.dumps(output_dict, indent=4, sort_keys=True))

#  dict of lists of dicts
expected_output = {
    "TMUS": [
        {
            "closing": "200.00",
            "date": "2020-12-30",
        },
        {
            "closing": "220.00",
            "date": "2020-12-31",
        }
    ],

    "MSFT": [
        {
            "closing": "100.00",
            "date": "2020-12-30",
        },
        {
            "closing": "110.00",
            "date": "2020-12-31",
        }
    ]
}
