import csv

with open('CountyList.csv') as f:
    reader = csv.reader(f)
    CountyList = list(reader)
f.close()

with open('Income_by_County.csv') as f:
    reader = csv.reader(f)
    Income_Data = list(reader)
f.close()

with open('ExpandedIncome.csv', 'w') as out_file:
    for counties in CountyList:
        for incomes in Income_Data:
            income = ''
            if incomes[0] in counties[0]:
                income = incomes[1]
                break
        out_file.write("\"" + counties[0] + "\", " + income)
        out_file.write("\n")
out_file.close()
