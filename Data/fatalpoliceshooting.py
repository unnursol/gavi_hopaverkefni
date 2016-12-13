import csv
import datetime
file = open('./data/fatal_police_shootings.csv')

dataStorage = csv.DictReader(file)

data = []
for i in dataStorage:
    data.append(i)

file.close()

for i in data:
	i['city'].replace("'","")

outfile = open('insertstatementsForFatalPoliceShootings.sql', 'w')

for i in data:
    outfile.write("insert into fatalPoliceShootings (time, causeOfDeath, state, city) values ({}, '{}', '{}', '{}');\n".format(int(datetime.datetime.strptime(i['date'], "%Y-%m-%d").timestamp()), i['manner_of_death'], i['state'], i['city'] ))

outfile.close()
