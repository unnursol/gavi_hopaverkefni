import csv
import datetime
file = open('911.csv')

dataStorage = csv.DictReader(file)

data = []
for i in dataStorage:
    data.append(i)

file.close()

outfile = open('insertstatementsFor911Calls.sql', 'w')

for i in data:
    outfile.write("insert into emergencyCalls (time, address) values ('{}', '{}');\n".format(str(i['timeStamp']).replace('-', '/').split()[0], i['addr'] ))

outfile.close()
