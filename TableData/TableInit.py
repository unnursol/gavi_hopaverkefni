import datetime
import connection
import helper_functions

cursor, conn = connection.connectToDatabase()
moons = connection.readFromFile('moon-phases-1970-2015-America_New_York.csv')
crimes = connection.readFromFile('Crimes_-_2001_to_present.csv')
emergencyCalls = connection.readFromFile('911.csv')
fatalPoliceShootings = connection.readFromFile('fatal_police_shootings.csv')
drugRelatedDeaths = connection.readFromFile('Accidental_Drug_Related_Deaths__2012-_June_2016.csv')

insertToMoons(moons)
insertToOffenses(crimes)
insertToCrimes(crimes)

#----------------------------------------------------------------------------
#                              Moon Phases
#----------------------------------------------------------------------------
def insertToMoons(sunAndMoon):
    insertstring = "insert into moons (phase, time) values "
    values = []
    for i in sunAndMoon:
        values.append((i['phase'], i['timestamp']))

    args_str = b','.join(cursor.mogrify("(%s,%s)", x) for x in values)
    cursor.execute(insertstring + args_str.decode('utf-8'))
    conn.commit()

#----------------------------------------------------------------------------
#                                 Crimes
#----------------------------------------------------------------------------

#-------------------------------  Offenses ----------------------------------
def insertToOffenses(crimes):
    insertstring = "insert into offenses(offense) values (%s);"
    offenses = set()
    for i in crimes:
        offenses.add(i['Primary Type'])
    list(offenses)
    for i in offenses:
        cursor.execute(insertstring, [i])
    conn.commit()

def insertToCrimes(crimes):
    select = "select * from offenses;"
    cursor.execute(select)
    records = cursor.fetchall()

    offense_id = {}
    for i in records:
        offense_id[i[1]] = i[0]

    insertstring = "insert into crimes (time, offense_id, method) values"
    values = []
    for i in crimes:
        off_id = offense_id[ i['Primary Type'] ]
        method = 'method'
        time = int(datetime.datetime.strptime(i['Date'], "%m/%d/%Y %I:%M:%S %p").timestamp())
        values.append((time, off_id, method))

    args_str = b','.join(cursor.mogrify("(%s,%s,%s)", x) for x in values)
    cursor.execute(insertstring + args_str.decode('utf-8'))
    conn.commit()

#----------------------------------------------------------------------------
#                                911 calls
#----------------------------------------------------------------------------
def insertToEmergencyCalls(emergencyCalls):
    insertstring = "insert into emergencyCalls (time, address) values "
    values = []
    for i in emergencyCalls:
        values.append((int(datetime.datetime.strptime(i['timeStamp'], "%Y-%m-%d %H:%M:%S").timestamp()), i['addr'] ))
    args_str = b','.join(cursor.mogrify("(%s,%s)", x) for x in values)
    cursor.execute(insertstring + args_str.decode('utf-8'))
    conn.commit()

#----------------------------------------------------------------------------
#                           Fatal police shootings
#----------------------------------------------------------------------------
def insertToCities(fatalPoliceShootings, drugRelatedDeaths):
    insertstring = "insert into cities(city) values ;"
    cities = set()
    for i in fatalPoliceShootings:
        cities.add(i['city'])
    for i in drugRelatedDeath:
        cities.add(i['Death City'])

    list(cities)
    args_str = b','.join(cursor.mogrify("(%s,%s)", x) for x in cities)
    cursor.execute(insertstring + args_str.decode('utf-8'))
    conn.commit()

def insertToFatalPoliceShootings(fatalPoliceShootings):
    select = "select * from cites;"
    cursor.execute(select)
    records = cursor.fetchall()

    city_id = {}
    for i in records:
        city_id[i[1]] = i[0]

    insertstring = "insert into fatalPoliceShootings (time, causeOfDeath, state, city_id) values "
    values = []
    for i in fatalPoliceShootings:
        cit_id = city_id[ i['city'] ]
        time = int(datetime.datetime.strptime(i['date'], "%Y-%m-%d").timestamp())
        causeOfDeath = i['manner_of_death']
        state = i['state']
        values.append((time, causeOfDeath, state, cit_id))

    args_str = b','.join(cursor.mogrify("(%s,%s,%s,%s)", x) for x in values)
    cursor.execute(insertstring + args_str.decode('utf-8'))
    conn.commit()

#----------------------------------------------------------------------------
#                             Drug related deaths
#----------------------------------------------------------------------------

def insertToDrugRelatedDeaths(drugRelatedDeaths):
    select = "select * from cites;"
    cursor.execute(select)
    records = cursor.fetchall()

    city_id = {}
    for i in records:
        city_id[i[1]] = i[0]

    for i in drugRelatedDeaths:
    	if i['Date'] is '':
    		drugRelatedDeaths.remove(i)

    insertstring = "insert into drugDeaths (time, sex, age, race, cause, city_id) values "
    values = []
    for i in drugRelatedDeaths:
        time = str(i['Date'])
        cit_id = city_id[ i['Death City'] ]
        sex = i['Sex']
        age = i['Age']
        race = i['Race']
        cause = i['ImmediateCauseA']
        values.append((time, sex, age, race, cause, cit_id))

    args_str = b','.join(cursor.mogrify("(%s,%s,%s,%s,%s,%s)", x) for x in values)
    cursor.execute(insertstring + args_str.decode('utf-8'))
    conn.commit()

conn.commit()
cursor.close()
conn.close()
