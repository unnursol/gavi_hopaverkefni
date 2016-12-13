import csv
import datetime
file = open('crime_homicide_subset.csv')

dataStoreage = csv.DictReader(file) 

data = []
for x in dataStoreage:
	data.append(x)

file.close()

outfile = open('insertstatementsForCrimes.sql', 'w')

for i in data:
	outfile.write("insert into crimes (time, offense, method) values ({}, '{}', '{}');\n".format(int(datetime.datetime.strptime(i['REPORT_DAT'], "%m/%d/%Y %H:%M").timestamp()), i['OFFENSE'], i['METHOD'] ))

outfile.close()