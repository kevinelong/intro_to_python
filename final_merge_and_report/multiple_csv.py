import csv

sources = [
    "./incoming/mail_source1.csv",
    "./incoming/mail_source2.csv",
]

merged = []
for s in sources:
    data = list(csv.reader(open(s)))
    rows = data[1:]  # skip the first row
    for row in rows:
        merged.append(row)
print(len(merged))
print(merged)
