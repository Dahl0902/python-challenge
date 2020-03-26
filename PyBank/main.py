import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

dates = []
PandL = []
profit = 0
loss = 0
rowc = 0
total = 0

with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
    for row in csvreader:
        rowc = rowc + 1
        PandL.append(row[1])
        dates.append(row)
    PandL = list(map(int, PandL))
    total = sum(PandL)
    average = (total/(rowc-1))
    decrease = min(PandL)
    dindex = PandL.index(decrease)
    ddate = dates[dindex]
    increase = max(PandL)
    iindex = PandL.index(increase)
    idate = dates[iindex]
print('Financial Analysis')
print('-----------------------------')
print('Total Months:' + str(rowc))
print('Total: $' + str(total))
print('Average Change: $' + str(average))
print('Greatest Increase in Profits: ' + str(idate))
print('Greatest Decrease in Profits: ' + str(ddate))

