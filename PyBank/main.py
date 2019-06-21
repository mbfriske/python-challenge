# Python Homework - PyBank (Matt Friske)

import os
import csv

print ("Hi, this is working")

csvpath = os.path.join("..\SMUDataScience⁩\SMUDAL201905DATA5⁩\02-Homework⁩\03-Python⁩\Instructions⁩\PyBank⁩\Resources⁩\budget_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")