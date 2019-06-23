# Python Homework - PyBank (Matt Friske)

import os
import csv
import numpy as np

csvpath = os.path.join("budget_data.csv")

total_month = 0
pl_total = 0
average_change_list = []
dates = []


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    first_row = next(csvreader)
    previous = int(first_row[1])
    total_month = total_month + 1 
    pl_total = pl_total + int(first_row[1])
    dates.append(first_row[0])

    for row in csvreader:
        total_month = total_month + 1 
        pl_total = pl_total + int(row[1])
   
        average_change = int(row[1]) - previous
        average_change_list.append(average_change)
        previous = int(row[1])
        dates.append(row[0])
        

average_change_calc = (sum(average_change_list) / (len(average_change_list)))


maxIndx = np.argmax(average_change_list) + 1
minIndx = np.argmin(average_change_list) + 1

maxDate = dates[maxIndx]
minDate = dates[minIndx]


print("Financial Analysis")
print("---------------------------------------")
print("Total Months: " + str(total_month))
print("Total: " + "$" + str(pl_total))
print(f"Average Change: ${round(average_change_calc, 2)}")
print("Greatest Increse in Profits: " + str(maxDate) + " ($" + str(max(average_change_list)) + ")")
print("Greatest Decrease in Profits: " + str(minDate) + " ($" + str(min(average_change_list)) + ")")

fh = open("bankpy_text", "w")

fh.write("Financial Analysis\n")
fh.write("---------------------------------------\n")
fh.write("Total Months: " + str(total_month) + "\n")
fh.write("Total: " + "$" + str(pl_total) + "\n")
fh.write("Average Change: $" + str(round(average_change_calc, 2)) + "\n")
fh.write("Greatest Increse in Profits: " + str(maxDate) + " ($" + str(max(average_change_list)) + ")\n")
fh.write("Greatest Decrease in Profits: " + str(minDate) + " ($" + str(min(average_change_list)) + ")\n")

fh.close()

                