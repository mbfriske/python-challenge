# Python Homework - PyPoll (Matt Friske)

import os
import csv

csvpath = os.path.join("election_data.csv")

total = 0
candidate_list = []
khan = []
correy = []
li = []
otooley = []


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    khan_count = 1
    correy_count = 1
    li_count = 1
    otooley_count = 1
    total = total + 1

    for row in csvreader:
        total = total + 1
        candidate_list.append(row[2])

        if row[2] == "Khan":
            khan.append(khan_count)

        if row[2] == "Correy":
            correy.append(correy_count)

        if row[2] == "Li":
            li.append(li_count)

        if row[2] == "O'Tooley":
            otooley.append(otooley_count)


khan_sum = sum(khan)
correy_sum = sum(correy)
li_sum = sum(li)
otooley_sum = sum(otooley)

winner = "none"
if khan_sum > correy_sum and khan_sum > li_sum and khan_sum > otooley_sum:
    winner = "Khan"

if correy_sum > khan_sum and correy_sum > li_sum and correy_sum > otooley_sum:
    winner = "Correy"

if li_sum > khan_sum and li_sum > correy_sum and li_sum > otooley_sum:
    winner = "Li"

if otooley_sum > khan_sum and otooley_sum > correy_sum and otooley_sum > li_sum:
    winner = "O'Tooley"

khan_per = khan_sum / total
correy_per = correy_sum / total
li_per = li_sum / total
otooley_per = otooley_sum / total


print("Election Results")
print("----------------------")
print("Total Votes: " + str(total))
print("Khan: " + str("{:.3%}".format(khan_per)) + " (" + str(khan_sum) + ")")
print("Correy: " + str("{:.3%}".format(correy_per)) + " (" + str(correy_sum) + ")")
print("Li: " + str("{:.3%}".format(li_per)) + " (" + str(li_sum) + ")")
print("O'Tooley: " + str("{:.3%}".format(otooley_per)) + " (" + str(otooley_sum) + ")")
print("----------------------")
print("Winner: " + str(winner))
print("----------------------")


fh = open("pypoll_text", "w")

fh.write("Election Results\n")
fh.write("----------------------\n")
fh.write("Total Votes: " + str(total) + "\n")
fh.write("Khan: " + str("{:.3%}".format(khan_per)) + " (" + str(khan_sum) + ")\n")
fh.write("Correy: " + str("{:.3%}".format(correy_per)) + " (" + str(correy_sum) + ")\n")
fh.write("Li: " + str("{:.3%}".format(li_per)) + " (" + str(li_sum) + ")\n")
fh.write("O'Tooley: " + str("{:.3%}".format(otooley_per)) + " (" + str(otooley_sum) + ")\n")
fh.write("----------------------\n")
fh.write("Winner: " + str(winner) + "\n")
fh.write("----------------------\n")

fh.close()
