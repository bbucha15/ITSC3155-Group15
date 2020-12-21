import json
import csv

with open('CountyList.csv') as f:
    reader = csv.reader(f)
    CountyList = list(reader)
f.close()

with open('Population_Data.csv') as f:
    reader = csv.reader(f)
    Population_Data = list(reader)
f.close()

with open('Income_by_County.csv') as f:
    reader = csv.reader(f)
    Income_Data = list(reader)
f.close()

with open('ISP_Percent.csv') as f:
    reader = csv.reader(f)
    ISP_Percent = list(reader)
f.close()

with open("NCSC_Counties_Population_Income_Coverage.geojson",'w') as out_file:

    out_file.write("{\"type\": \"FeatureCollection\",\"features\": [")
    out_file.write("\n")

    with open("allCounties.geojson") as json_file:
        allCounties = json.load(json_file)

        for x in allCounties['features']:
            if (x['properties']['STATEFP']) == "45" or (x['properties']['STATEFP']) == "37":
                for counties in CountyList:
                    if (x['properties']['NAME']) in counties[0]:
                        county = counties[0]
                        break

                for populations in Population_Data:
                    if (x['properties']['NAME']) in populations[0]:
                        population = populations[1]
                        break

                for incomes in Income_Data:
                    if (x['properties']['NAME']) in incomes[0]:
                        income = incomes[1]
                        break

                for percents in ISP_Percent:
                    if (x['properties']['NAME']) in percents[0]:
                        percent = percents[1]
                        break

                x['properties'] = {"Name": county, "Population": int(population), "Median_Income": int(income),
                                   "ISP_Coverage": float(percent)}

                out_file.write(str(x)+",")
                out_file.write("\n")
    out_file.write("]}")
