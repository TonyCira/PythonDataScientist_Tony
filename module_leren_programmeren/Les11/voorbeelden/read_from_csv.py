import csv
from tabulate import tabulate

with open("university_records.csv", "r", newline="") as f:
    data = csv.reader(f)
    headers = next(data)
    rijen = list(data)          # de rest als lijst van lijsten

print(tabulate(rijen, headers=headers, showindex=True))