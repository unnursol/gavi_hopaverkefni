import datetime
import connection
import helper_functions

cursor, conn = connection.connectToDatabase()
moons = connection.readFromFile('moon-phases-1970-2015-America_New_York.csv')
crimes = connection.readFromFile('Crimes_-_2001_to_present.csv')
emergencyCalls = connection.readFromFile('911.csv')
fatalPoliceShootings = connection.readFromFile('fatal_police_shootings.csv')
drugRelatedDeaths = connection.readFromFile('Accidental_Drug_Related_Deaths__2012-_June_2016.csv')


#----------------------------------------------------------------------------
#                              Moon Phases
#----------------------------------------------------------------------------
def insertToMoons(sunAndMoon):
    insertstring = "insert into moons (phase, time) values "
    values = []
    for i in sunAndMoon:
        values.append((i['phase'], datetime.datetime.fromtimestamp(int(i['timestamp'])).strftime('%d/%m/%Y')))

    args_str = b','.join(cursor.mogrify("(%s,%s)", x) for x in values)
    cursor.execute('SET datestyle = dmy')
    cursor.execute(insertstring + args_str.decode('utf-8'))
    conn.commit()

#----------------------------------------------------------------------------
#                                 Crimes
#----------------------------------------------------------------------------
def insertToCrimes(crimes, offense_id):
    insertstring = "insert into crimes (time, offense_id) values"
    values = []
    for i in crimes:
        off_id = offense_id[ i['Primary Type'] ]
        date = str(i['Date']).split()[0].split('/')
        newDate = []
        newDate.append(date[1])
        newDate.append(date[0])
        newDate.append(date[2])
        time = '/'.join(newDate)
        values.append((time, off_id))

    args_str = b','.join(cursor.mogrify("(%s,%s)", x) for x in values)
    cursor.execute('SET datestyle = dmy')
    cursor.execute(insertstring + args_str.decode('utf-8'))
    conn.commit()

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

#----------------------------------------------------------------------------
#                                911 calls
#----------------------------------------------------------------------------
def insertToEmergencyCalls(emergencyCalls):
    insertstring = "insert into emergencyCalls (time, address) values "
    values = []
    for i in emergencyCalls:
        values.append((str(i['timeStamp']).replace('-', '/').split()[0], i['addr']))
    args_str = b','.join(cursor.mogrify("(%s,%s)", x) for x in values)
    cursor.execute(insertstring + args_str.decode('utf-8'))
    conn.commit()

#----------------------------------------------------------------------------
#                           Fatal police shootings
#----------------------------------------------------------------------------
def insertToFatalPoliceShootings(fatalPoliceShootings, city_id):
    insertstring = "insert into fatalPoliceShootings (time, causeOfDeath, state, city_id) values "
    values = []
    for i in fatalPoliceShootings:
        cit_id = city_id[ i['city'] ]
        time = str(i['date'])
        causeOfDeath = i['manner_of_death']
        state = i['state']
        values.append((time, causeOfDeath, state, cit_id))

    args_str = b','.join(cursor.mogrify("(%s,%s,%s,%s)", x) for x in values)
    cursor.execute(insertstring + args_str.decode('utf-8'))
    conn.commit()

#-------------------------------- Cities ------------------------------------
def insertToCities(fatalPoliceShootings, drugRelatedDeath):
    insertstring = "insert into cities(city) values (%s);"
    cities = set()
    for i in fatalPoliceShootings:
        cities.add(i['city'])
    for i in drugRelatedDeath:
        cities.add(i['Death City'])

    list(cities)

    for i in cities:
        cursor.execute(insertstring, [i])
    conn.commit()

#----------------------------------------------------------------------------
#                             Drug related deaths
#----------------------------------------------------------------------------

def insertToDrugRelatedDeaths(drugRelatedDeaths, city_id):

    for i in drugRelatedDeaths:
    	if i['Date'] is '':
    		drugRelatedDeaths.remove(i)

    insertstring = "insert into drugDeaths (time, sex, age, race, cause, city_id) values "
    values = []
    for i in drugRelatedDeaths:
        date = str(i['Date']).split('/')
        newDate = []
        newDate.append(date[1])
        newDate.append(date[0])
        newDate.append(date[2])
        time = '/'.join(newDate)
        cit_id = city_id[ i['Death City'] ]
        sex = i['Sex']
        age = i['Age']
        race = i['Race']
        cause = i['ImmediateCauseA']
        values.append((time, sex, age, race, cause, cit_id))

    args_str = b','.join(cursor.mogrify("(%s,%s,%s,%s,%s,%s)", x) for x in values)
    cursor.execute('SET datestyle = dmy')
    cursor.execute(insertstring + args_str.decode('utf-8'))
    conn.commit()

insertToOffenses(crimes)
insertToCities(fatalPoliceShootings, drugRelatedDeaths)
city_id = helper_functions.getIds('cities', cursor)
offense_id = helper_functions.getIds('offenses', cursor)

insertToMoons(moons)
insertToCrimes(crimes, offense_id)
insertToEmergencyCalls(emergencyCalls)
insertToDrugRelatedDeaths(drugRelatedDeaths, city_id)
insertToFatalPoliceShootings(fatalPoliceShootings, city_id)

conn.commit()
cursor.close()
conn.close()
