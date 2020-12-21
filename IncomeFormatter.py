import csv

lastCounty = ""
numZips = 1
totalIncome = 0
totalIndiv = 0

with open('ZipLookup.csv') as Zip_file:
    csv_reader = csv.reader(Zip_file, delimiter=',')
    zip_dict = {rows[0]: rows[1] for rows in csv_reader}
Zip_file.close()

with open('Income_data.csv', 'w') as out_file:

    #ZIPCODE,Num Indiv,Avg Income
    with open('Income_Stats_by_Zip.csv') as Income_file:
        Income_reader = csv.reader(Income_file, delimiter=',')
        for row in Income_reader:

            numZips = numZips + 1
            totalIndiv = totalIndiv + int(row[1])
            totalIncome = totalIncome + int(row[2])
            if lastCounty == zip_dict.get(row[0]):
                continue
            else:
                avgIncome = totalIncome / numZips
                out_file.write("\"" + str(lastCounty) + "\"" + "," + str(totalIndiv) + "," + str(round(avgIncome)))
                out_file.write("\n")

                numZips = 1
                totalIncome = 0
                totalIndiv = 0
            lastCounty = zip_dict.get(row[0])
    Income_file.close()
out_file.close()