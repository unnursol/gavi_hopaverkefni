import csv
import psycopg2
import getpass
import datetime

def readFromFile(filename):
    file = open(filename)
    dataStoreage = csv.DictReader(file)
    data = []
    for x in dataStoreage:
    	data.append(x)
    file.close()
    return data

def connectToDatabase():
    host = 'localhost'
    dbname = input('Database name: ')
    username = input('User name for {}.{}: '.format(host,dbname))

    #pw = getpass.getpass()
    pw = input('pw: ')

    conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(host, dbname, username, pw)

    print("Connecting to database {}.{} as {}".format(host, dbname, username))

    try:
        conn = psycopg2.connect(conn_string)
    except psycopg2.OperationalError as e:
        print('Connection failed!')
        print('Error message:', e)
        exit()

    cursor = conn.cursor()
    print("Connected!\n")

    return cursor, conn

cursor, conn = connectToDatabase()
sunAndMoon = readFromFile('moon-phases-1970-2015-America_New_York.csv')
crimes = readFromFile('Crimes_-_2001_to_present.csv')
emergencyCalls = readFromFile('911.csv')
fatalPoliceShootings = readFromFile('fatal_police_shootings.csv')
drugRelatedDeaths = readFromFile('Accidental_Drug_Related_Deaths__2012-_June_2016.csv')

print(crimes[0])
print(emergencyCalls[0])

#----------------------------------------------------------------------------
#                              Moon Phases
#----------------------------------------------------------------------------
insertstring = "insert into moons (phase, time) values "
values = []
for i in sunAndMoon:
    values.append((i['phase'], i['timestamp']))

args_str = b','.join(cursor.mogrify("(%s,%s)", x) for x in values)
cursor.execute(insertstring + args_str.decode('utf-8'))

#----------------------------------------------------------------------------
#                                 Crimes
#----------------------------------------------------------------------------
insertstring = "insert into crimes (time, offense) values "
valuesCrimes = []
valuesOffenses = []
#-------------------------------  Offenses ----------------------------------

for i in crimes:
    valuesCrimes.append((int(datetime.datetime.strptime(i['Date'], "%m/%d/%Y %I:%M:%S %p").timestamp()), i['Primary Type']))

args_str = b','.join(cursor.mogrify("(%s,%s)", x) for x in values)
cursor.execute(insertstring + args_str.decode('utf-8'))

#----------------------------------------------------------------------------
#                                911 calls
#----------------------------------------------------------------------------
insertstring = "insert into emergencyCalls (time, address) values "
values = []
for i in emergencyCalls:
    values.append((int(datetime.datetime.strptime(i['timeStamp'], "%Y-%m-%d %H:%M:%S").timestamp()), i['addr'] ))
args_str = b','.join(cursor.mogrify("(%s,%s)", x) for x in values)
cursor.execute(insertstring + args_str.decode('utf-8'))

#----------------------------------------------------------------------------
#                           Fatal police shootings
#----------------------------------------------------------------------------


#----------------------------------------------------------------------------
#                             Drug related deaths
#----------------------------------------------------------------------------

conn.commit()
cursor.close()
conn.close()
