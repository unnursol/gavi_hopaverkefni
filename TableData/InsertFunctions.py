from HelperFunctions import fixTitle, fixOffense
import datetime

#----------------------------------------------------------------------------
#                              Moon Phases
#----------------------------------------------------------------------------
def insertToMoons(sunAndMoon, cursor, conn):
    insertstring = "insert into moons (phase, time) values "
    values = []
    numberofrowstoinsert = 2000
    counter = 0
    for i in sunAndMoon:
        values.append((i['phase'], datetime.datetime.fromtimestamp(int(i['timestamp'])).strftime('%d/%m/%Y')))
        counter += 1

        if counter == numberofrowstoinsert:
            args_str = b','.join(cursor.mogrify("(%s,%s)", x) for x in values)
            cursor.execute('SET datestyle = dmy')
            cursor.execute(insertstring + args_str.decode('utf-8'))
            values = []
            counter = 0

    if len(values) > 0:
        args_str = b','.join(cursor.mogrify("(%s,%s)", x) for x in values)
        cursor.execute('SET datestyle = dmy')
        cursor.execute(insertstring + args_str.decode('utf-8'))
        values = []
        counter = 0

    conn.commit()

#----------------------------------------------------------------------------
#                                 Crimes
#----------------------------------------------------------------------------
def insertToCrimes(crimes, offense_id, cursor, conn):
    insertstring = "insert into crimes (time, offense_id) values"
    values = []
    numberofrowstoinsert = 2000
    counter = 0
    for i in crimes:
        tmp = fixOffense(i['Primary Type'])
        off_id = offense_id[ tmp ]
        date = str(i['Date']).split()[0].split('/')
        newDate = []
        newDate.append(date[1])
        newDate.append(date[0])
        newDate.append(date[2])
        time = '/'.join(newDate)
        values.append((time, off_id))
        counter += 1

        if counter == numberofrowstoinsert:
            args_str = b','.join(cursor.mogrify("(%s,%s)", x) for x in values)
            cursor.execute('SET datestyle = dmy')
            cursor.execute(insertstring + args_str.decode('utf-8'))
            values = []
            counter = 0

    if len(values) > 0:
        args_str = b','.join(cursor.mogrify("(%s,%s)", x) for x in values)
        cursor.execute('SET datestyle = dmy')
        cursor.execute(insertstring + args_str.decode('utf-8'))
        values = []
        counter = 0

    conn.commit()

#-------------------------------  Offenses ----------------------------------
def insertToOffenses(crimes, cursor, conn):
    insertstring = "insert into offenses (offense) values (%s);"
    offenses = set()
    for i in crimes:
        tmp = fixOffense(i['Primary Type'])
        offenses.add(tmp)
    list(offenses)
    for i in offenses:
        cursor.execute(insertstring, [i])
    conn.commit()

#----------------------------------------------------------------------------
#                                911 calls
#----------------------------------------------------------------------------
def insertToEmergencyCalls(emergencyCalls, cursor, conn):
    insertstring = "insert into emergencyCalls (time, address) values "
    values = []
    numberofrowstoinsert = 2000
    counter = 0
    for i in emergencyCalls:
        values.append((str(i['timeStamp']).replace('-', '/').split()[0], i['addr']))
        counter += 1

        if counter == numberofrowstoinsert:
            args_str = b','.join(cursor.mogrify("(%s,%s)", x) for x in values)
            cursor.execute(insertstring + args_str.decode('utf-8'))
            values = []
            counter = 0

    if len(values) > 0:
        args_str = b','.join(cursor.mogrify("(%s,%s)", x) for x in values)
        cursor.execute(insertstring + args_str.decode('utf-8'))
        values = []
        counter = 0

    conn.commit()

#----------------------------------------------------------------------------
#                           Fatal police shootings
#----------------------------------------------------------------------------
def insertToFatalPoliceShootings(fatalPoliceShootings, city_id, cursor, conn):
    insertstring = "insert into fatalPoliceShootings (time, causeOfDeath, state, city_id) values "
    values = []
    numberofrowstoinsert = 2000
    counter = 0
    for i in fatalPoliceShootings:
        tmp  = fixTitle(i['city'])
        cit_id = city_id[ tmp ]
        time = str(i['date'])
        causeOfDeath = i['manner_of_death']
        state = i['state']
        values.append((time, causeOfDeath, state, cit_id))
        counter += 1

        if counter == numberofrowstoinsert:
            args_str = b','.join(cursor.mogrify("(%s,%s,%s,%s)", x) for x in values)
            cursor.execute(insertstring + args_str.decode('utf-8'))
            values = []
            counter = 0

    if len(values) > 0:
        args_str = b','.join(cursor.mogrify("(%s,%s,%s,%s)", x) for x in values)
        cursor.execute(insertstring + args_str.decode('utf-8'))
        values = []
        counter = 0

    conn.commit()

#-------------------------------- Cities ------------------------------------
def insertToCities(fatalPoliceShootings, drugRelatedDeath, cursor, conn):
    insertstring = "insert into cities(city) values (%s);"
    cities = set()
    for i in fatalPoliceShootings:
        tmp  = fixTitle(i['city'])
        cities.add(tmp)
    for i in drugRelatedDeath:
        tmp  = fixTitle(i['Death City'])
        cities.add(tmp)

    list(cities)

    for i in cities:
        cursor.execute(insertstring, [i])
    conn.commit()

#----------------------------------------------------------------------------
#                             Drug related deaths
#----------------------------------------------------------------------------

def insertToDrugRelatedDeaths(drugRelatedDeaths, city_id, cursor, conn):

    for i in drugRelatedDeaths:
    	if i['Date'] is '':
    		drugRelatedDeaths.remove(i)

    insertstring = "insert into drugDeaths (time, sex, age, race, cause, city_id) values "
    values = []
    numberofrowstoinsert = 2000
    counter = 0
    for i in drugRelatedDeaths:
        date = str(i['Date']).split('/')
        newDate = []
        newDate.append(date[1])
        newDate.append(date[0])
        newDate.append(date[2])
        time = '/'.join(newDate)
        tmp  = fixTitle(i['Death City'])
        cit_id = city_id[ tmp ]
        sex = i['Sex']
        age = i['Age']
        race = i['Race']
        cause = fixTitle(i['ImmediateCauseA'])
        values.append((time, sex, age, race, cause, cit_id))
        counter += 1

        if counter == numberofrowstoinsert:
            args_str = b','.join(cursor.mogrify("(%s,%s,%s,%s,%s,%s)", x) for x in values)
            cursor.execute('SET datestyle = dmy')
            cursor.execute(insertstring + args_str.decode('utf-8'))
            values = []
            counter = 0

    if len(values) > 0:
        args_str = b','.join(cursor.mogrify("(%s,%s,%s,%s,%s,%s)", x) for x in values)
        cursor.execute('SET datestyle = dmy')
        cursor.execute(insertstring + args_str.decode('utf-8'))
        values = []
        counter = 0

    conn.commit()
