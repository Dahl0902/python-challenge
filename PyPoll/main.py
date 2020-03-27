import os  
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

votes = 0
kvotes = 0
cvotes = 0
lvotes = 0
ovotes = 0
errors = 0
kpercent = 0
cpercent = 0
lpercent = 0
opercent = 0
winner = 0
candidate = []
totalvotes = []

with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
    for row in csvreader:
        votes = votes + 1
        candidate.append(row[2])
    for person in candidate:
        if person == "Khan":
            kvotes += 1
        elif person == "Correy":
            cvotes += 1
        elif person == "Li":
            lvotes += 1
        elif person == "O'Tooley":
            ovotes += 1
        else:
            errors += 1
    kpercent = (kvotes / votes) * 100
    cpercent = (cvotes / votes) * 100
    lpercent = (lvotes / votes) * 100
    opercent = (ovotes / votes) * 100

    kpercent = round(kpercent, 3)
    cpercent = round(cpercent, 3)
    lpercent = round(lpercent, 3)
    opercent = round(opercent, 3)

    dcan = {kvotes: "Khan",
    cvotes: "Correy",
    lvotes: "Li",
    ovotes: "O'Tooley"}

    totalvotes = [kvotes, cvotes, lvotes, ovotes]
    for i in totalvotes:
        for j in totalvotes:
            if i > j and i > winner:
                winner = i

f = open("Election_Results.txt" , 'w')

print('Election Results', file=f)
print('------------------------------', file=f)
print('Total Votes: ' + str(votes), file=f)
print('------------------------------', file=f)
print('Khan: ' + str(kpercent) + '%' + ' (' + str(kvotes) + ')', file=f)
print('Correy: ' + str(cpercent) + '%' + ' (' + str(cvotes) + ')', file=f)
print('Li: ' + str(lpercent) + '%' + ' (' + str(lvotes) + ')', file=f)
print("O'Tooley: " + str(opercent) + '%' + ' (' + str(ovotes) + ')', file=f)
print('------------------------------', file=f)
print('Winner: ' + dcan[winner], file=f)
print('------------------------------', file=f)

f.close()

print('Election Results')
print('------------------------------')
print('Total Votes: ' + str(votes))
print('------------------------------')
print('Khan: ' + str(kpercent) + ' (' + str(kvotes) + ')')
print('Correy: ' + str(cpercent) + ' (' + str(cvotes) + ')')
print('Li: ' + str(lpercent) + ' (' + str(lvotes) + ')')
print("O'Tooley: " + str(opercent) + ' (' + str(ovotes) + ')')
print('------------------------------')
print('Winner: ' + dcan[winner])
print('------------------------------')
