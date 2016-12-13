import csv
import datetime
file = open('Data\Accidental_Drug_Related_Deaths__2012-_June_2016.csv')

dataStorage = csv.DictReader(file)

data = []

for row in dataStorage:
	data.append(row)

file.close()

for i in data:
	if i['Date'] is '':
		data.remove(i)

outfile = open('insertstatementsForAccidentalDrugRelatedDeaths.sql', 'w')

for i in data:
	outfile.write("insert into drugDeaths (time, sex, age, race, cause, deathcity) values ({}, '{}', '{}', '{}', '{}', '{}');\n".format(int(datetime.datetime.strptime(i['Date'], "%m/%d/%Y").timestamp()), i['Sex'], i['Age'], i['Race'], i['ImmediateCauseA'], i['Death City']))

outfile.close()
