import csv
import datetime
file = open('./data/911.csv')

dataStorage = csv.DictReader(file)

data = []
for i in dataStorage:
    data.append(i)

file.close()

outfile = open('insertstatementsFor911Calls.sql', 'w')

for i in data:
    outfile.write("insert into emergencyCalls (time, address) values ({}, '{}');\n".format(int(datetime.datetime.strptime(i['timeStamp'], "%Y-%m-%d %H:%M:%S").timestamp()), i['addr'] ))

outfile.close()
