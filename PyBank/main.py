import os
import csv


csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

dates = []
PandL = []
profit = 0
loss = 0
rowc = 0
total = 0
average = 0
change = 0

with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
    for row in csvreader:
        rowc = rowc + 1
        PandL.append(row[1])
        dates.append(row)
    PandL = list(map(int, PandL))
    total = sum(PandL)
    first = PandL[0]
    last = PandL[(rowc - 1)]
    change = (last - first)
    average = (change/(rowc-1))
    decrease = min(PandL)
    dindex = PandL.index(decrease)
    ddate = dates[dindex]
    increase = max(PandL)
    iindex = PandL.index(increase)
    idate = dates[iindex]
average = round(average, 2)
f = open("Financial_Analysis.txt" , 'w')

print('Financial Analysis', file=f)
print('------------------------------', file=f)
print('Total Months:' + str(rowc), file=f)
print('Total: $' + str(total), file=f)
print('Average Change: $' + str(average), file=f)
print('Greatest Increase in Profits: ' + str(idate), file=f)
print('Greatest Decrease in Profits: ' + str(ddate), file=f)

f.close()

print('Financial Analysis')
print('------------------------------')
print('Total Months:' + str(rowc))
print('Total: $' + str(total))
print('Average Change: $' + str(average))
print('Greatest Increase in Profits: ' + str(idate))
print('Greatest Decrease in Profits: ' + str(ddate))