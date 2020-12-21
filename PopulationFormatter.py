import csv

with open('Population_Data.csv', 'w') as out_file:

    with open('PopulationByCounty.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if "North Carolina" in row[0] or "South Carolina" in row[0]:
                out_file.write("\""+row[0].strip(".")+"\""+","+row[1].replace(',', ''))
                out_file.write("\n")

    csv_file.close()
out_file.close()