import csv

countyNum = 0
geo_dict = {}
speedNum = 0

with open('GeoLookup.csv') as geo_file:
    csv_reader = csv.reader(geo_file, delimiter=',')
    geo_dict = {rows[0]: rows[1] for rows in csv_reader}
geo_file.close()

with open('ISP_data.csv', 'w') as out_file:

    # ['type', 'id', 'tech', 'urban_rural', 'tribal_non', 'speed', 'has_0', 'has_1', 'has_2', 'has_3more']
    with open('FCC_Wireline_Area_Table.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0] == 'county':
                out_file.write("\"" + geo_dict.get(row[1]) + "\"" + "," + row[5] + "," + row[6] + ","
                               + row[7] + "," + row[8] + "," + row[9])
                out_file.write("\n")
                if row[5] != 0.2:
                    speedNum = speedNum + 1

    csv_file.close()
out_file.close()
print(speedNum)
