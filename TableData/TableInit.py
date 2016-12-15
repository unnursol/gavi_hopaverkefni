import datetime
import csv
import psycopg2
import getpass
import datetime
import connection

cursor, conn = connection.connectToDatabase()
sunAndMoon = connection.readFromFile('moon-phases-1970-2015-America_New_York.csv')
crimes = connection.readFromFile('Crimes_-_2001_to_present.csv')
emergencyCalls = connection.readFromFile('911.csv')
fatalPoliceShootings = connection.readFromFile('fatal_police_shootings.csv')
drugRelatedDeaths = connection.readFromFile('Accidental_Drug_Related_Deaths__2012-_June_2016.csv')

print(crimes[0])
print(emergencyCalls[0])
#
# #----------------------------------------------------------------------------
# #                              Moon Phases
# #----------------------------------------------------------------------------
# insertstring = "insert into moons (phase, time) values "
# values = []
# for i in sunAndMoon:
#     values.append((i['phase'], i['timestamp']))
#
# args_str = b','.join(cursor.mogrify("(%s,%s)", x) for x in values)
# cursor.execute(insertstring + args_str.decode('utf-8'))

#----------------------------------------------------------------------------
#                                 Crimes
#----------------------------------------------------------------------------

#-------------------------------  Offenses ----------------------------------
insertstring = "insert into offenses(offense) values (%s);"
offenses = set()
for i in crimes:
    offenses.add(i['Primary Type'])

print(offenses[0])
print(offenses[-1])
# for i in offenses
#    cursor.execute(insertstring, [i])
# conn.commit()
#
# select = "select * from offenses;"
# cursor.execute(select)
# records = cursor.fetchall()
#
# offense_id = {}
# for i in records:
#     offense_id[i[1]] = i[0]
#
# insertstring = "insert into crimes (time, offense_id, method) values"
# values = []
# for i in crimes:
#     off_id = offense_id[ i['Primary Type'] ]
#     for key, value in i.items():
#         if not key == 'Primary Type':
#             method = i['method']
#             time = int(datetime.datetime.strptime(i['Date'], "%m/%d/%Y %I:%M:%S %p").timestamp())
#             values.append((time, off_id, method))
#
# args_str = b','.join(cursor.mogrify("(%s,%s, %s)", x) for x in values)
# cursor.execute(insertstring + args_str.decode('utf-8'))

# #----------------------------------------------------------------------------
# #                                911 calls
# #----------------------------------------------------------------------------
# insertstring = "insert into emergencyCalls (time, address) values "
# values = []
# for i in emergencyCalls:
#     values.append((int(datetime.datetime.strptime(i['timeStamp'], "%Y-%m-%d %H:%M:%S").timestamp()), i['addr'] ))
# args_str = b','.join(cursor.mogrify("(%s,%s)", x) for x in values)
# cursor.execute(insertstring + args_str.decode('utf-8'))
#
# #----------------------------------------------------------------------------
# #                           Fatal police shootings
# #----------------------------------------------------------------------------
# insertstring = "insert into fatalPoliceShootings (time, causeOfDeath, state, city) values "
# values = []
# for i in fatalPoliceShootings:
#     outfile.write("insert into fatalPoliceShootings (time, causeOfDeath, state, city) values ({}, '{}', '{}', '{}');\n".format(int(datetime.datetime.strptime(i['date'], "%Y-%m-%d").timestamp()), i['manner_of_death'], i['state'], i['city'] ))
#
# #----------------------------------------------------------------------------
# #                             Drug related deaths
# #----------------------------------------------------------------------------
# for i in drugRelatedDeaths:
# 	if i['Date'] is '':
# 		drugRelatedDeaths.remove(i)
#
# insertstring = "insert into drugDeaths (time, sex, age, race, cause, deathcity) values "
# values = []
# for i in drugRelatedDeaths:
# 	outfile.write("insert into drugDeaths (time, sex, age, race, cause, deathcity) values ('{}', '{}', '{}', '{}', '{}', '{}');\n".format(str(i['Date']), i['Sex'], i['Age'], i['Race'], i['ImmediateCauseA'], i['Death City']))

conn.commit()
cursor.close()
conn.close()
