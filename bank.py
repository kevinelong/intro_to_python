transactions = [
    {
        "name": "direct deposit",
        "amount": 1000
    },    {
        "name": "direct deposit",
        "amount": 200
    },    {
        "name": "withdrawl",
        "amount": -100
    },    {
        "name": "autopay",
        "amount": -300
    },
]
#SHOW ALL POSITIVE TRANSACTIONS
for item in transactions:
    if item["amount"] > 0:
        print(item)

#LATER SHOW ALL NEGATIVE TRANSACTIONS
for item in transactions:
    if item["amount"] < 0:
        print(item)

#SHOW THE TOTAL OF ALL POSITIVE AND NEGATIVE AMOUNT e.g. BALANCE
balance = 0
for item in transactions:
    balance += item["amount"]
print(balance)
# EXPECTED: 800

# CONVERT TO A LIST AND THEN USE SUM
amount_list = []
for item in transactions:
    amount_list.append(item["amount"])
print(sum(amount_list))

#SILLY
print(sum(
    [
        transactions[0]["amount"],
        transactions[1]["amount"],
        transactions[2]["amount"],
        transactions[3]["amount"]
    ]
    ))