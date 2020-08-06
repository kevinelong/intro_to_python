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
    if name not in list(output_dict):  # is key not in output dict? better create the key and assign empty list
        output_dict[name] = []  # Initialize new key in dict with empty list
    output_dict[name].append(s)
    del s["name"]
print(output_dict)

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
