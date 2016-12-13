import csv

file = open('moon-phases-1970-2015-America_New_York.csv')

dataStoreage = csv.DictReader(file)

data = []
for x in dataStoreage:
	data.append(x)

file.close()

outfile = open('insertstatementsForSunAndMoon.sql', 'w')

for i in data:
	outfile.write("insert into moons (phase, time) values ('{}', {});\n".format(i['phase'], i['timestamp']))

outfile.close()
