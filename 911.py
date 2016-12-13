import csv
import datetime
file = open('./data/911.csv')

dataStorage = csv.DictReader(file)

data = []
for i in dataStorage:
    data.append(x)

file.close()

outfile = open('insertstatementsFor911Calls.sql', 'w')

for i in data:
    outfile.write("insert into crimes (time, address) values ({}, '{}');\n".format(int(datetime.datetime.strptime(i['timeStamp'], "%m/%d/%Y %H:%M").timestamp()), i['addr'] ))

outfile.close()
