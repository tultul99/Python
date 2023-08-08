import csv
with open('tennis.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)
    print(your_list)

import csv
with open("results - 71.csv") as f:
    data = [r for r in csv.DictReader(f)]
