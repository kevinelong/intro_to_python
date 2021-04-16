"""

Run once an hour: (in python sleep and measure time that has past or Cron or windows Schedule-Task)

    Read from many sources POP3?

    Stage in CSV files.

    Merge into one and output somewhere (sql?)

    Summarize in python (use sql instead for most prod)

    Store summaries reports for later access

    Expose these in a GUI

"""
from clean_data import clean_matrix
from summarize import summarize
import json


def process_lines(lines, output, source):
    count = 0
    for line in lines:
        parts = line.split(",")
        if len(parts) == 6:
            count += 1
            if count > 1:
                parts.append(source)
                output.append(parts)
    return output


def read_sources():
    output = []

    sources = [
        "mail_source1.csv",
        "mail_source2.csv",
    ]
    root_folder = "./incoming/"

    for s in sources:
        f = open(root_folder + s, "r")
        lines = f.readlines()
        process_lines(lines, output, s)
    return output


results = read_sources()


data = """
ID,DATE_SENT,SENDER,RECIPIENT,SUBJECT,BODY
1,2020-12-30, kevin@example.com, alice@example.com,Demo,Now is the time...
2,2020-12-30, kevin@example.com, alice@example.com,Demo,Now is the time...
3,2020-12-29, bob@example.com, alice@example.com,Demo,Now is the time...
4,2020-12-29, bob@example.com, alice@example.com,Demo,Now is the time...
5,2020-12-29, info@example.com, alice@example.com,Demo,Now is the time...
"""
lines = data.split("\n")
process_lines(lines, results, "data")
# print(len(results))
# print(results)

expected = [['1', '2020-12-30', ' kevin@example.com', ' mary@example.com', 'Demo', 'Now is the time...\n', 'mail_source1.csv'], ['2', '2020-12-30', ' kevin@example.com', ' mary@example.com', 'Demo', 'Now is the time...\n', 'mail_source1.csv'], ['3', '2020-12-29', ' bob@example.com', ' mary@example.com', 'Demo', 'Now is the time...\n', 'mail_source1.csv'], ['4', '2020-12-29', ' bob@example.com', ' mary@example.com', 'Demo', 'Now is the time...\n', 'mail_source1.csv'], ['5', '2020-12-29', ' info@example.com', ' mary@example.com', 'Demo', 'Now is the time...\n', 'mail_source1.csv'], ['1', '2020-12-30', ' kevin@example.com', ' joe@example.com', 'Demo', 'Now is the time...\n', 'mail_source2.csv'], ['2', '2020-12-30', ' kevin@example.com', ' joe@example.com', 'Demo', 'Now is the time...\n', 'mail_source2.csv'], ['3', '2020-12-28', ' bob@example.com', ' joe@example.com', 'Demo', 'Now is the time...\n', 'mail_source2.csv'], ['4', '2020-12-28', ' sales@example.com', ' joe@example.com', 'Demo', 'Now is the time...\n', 'mail_source2.csv'], ['5', '2020-12-29', ' bob@example.com', ' joe@example.com', 'Demo', 'Now is the time...\n', 'mail_source2.csv'], ['1', '2020-12-30', ' kevin@example.com', ' alice@example.com', 'Demo', 'Now is the time...', 'data'], ['2', '2020-12-30', ' kevin@example.com', ' alice@example.com', 'Demo', 'Now is the time...', 'data'], ['3', '2020-12-29', ' bob@example.com', ' alice@example.com', 'Demo', 'Now is the time...', 'data'], ['4', '2020-12-29', ' bob@example.com', ' alice@example.com', 'Demo', 'Now is the time...', 'data'], ['5', '2020-12-29', ' info@example.com', ' alice@example.com', 'Demo', 'Now is the time...', 'data']]

# print(expected == results)


cleansed = clean_matrix(results)

# print(cleansed)

total = len(cleansed)
by_date = summarize(cleansed, 1) #date
by_sender = summarize(cleansed, 2) #sender


def export_to_file(data, name):
    f = open(f"final_merge_and_report/output/{name}.json", "w")
    f.write(json.dumps(data))


export_to_file(by_date, "by_date")
export_to_file(by_sender, "by_sender")
