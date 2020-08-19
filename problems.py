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

data = [12, 34, 10, 56, 78]
total = 0
#TOTAL
for n in data:
    total = total + n
    total += n

print(total)
print(sum(data))

#  HOW CAN WE GET THE LOWEST? LARGEST, AVERAGE?

# TOTAL ALL closing prices (use float(text) to a number)
#  create a dictionary of list of objects

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
