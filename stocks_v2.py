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


def split_list_to_dict(data, key="name"):
    output = {}

    for item in stocks:
        name = item[key]

        if name not in output:
            output[name] = []

        del item[key]

        output[name].append(item)
    return output


def display_dict(input_dict):
    for key in input_dict:
        print(f"{key}")
        item_list = input_dict[key]

        for item in item_list:
            print(item)


result = split_list_to_dict(stocks, key="date")
display_dict(result)
