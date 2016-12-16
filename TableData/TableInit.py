import connection
from HelperFunctions import getIds
from InsertFunctions import insertToMoons, insertToCrimes, insertToEmergencyCalls
from InsertFunctions import insertToDrugRelatedDeaths, insertToCities, insertToOffenses, insertToFatalPoliceShootings

#-------------------------------------------------------------------------------
#                   Connecting and reading data from files
#-------------------------------------------------------------------------------
cursor, conn = connection.connectToDatabase()
moons = connection.readFromFile('moon-phases-1970-2015-America_New_York.csv')
crimes = connection.readFromFile('Crimes_-_2001_to_present.csv')
emergencyCalls = connection.readFromFile('911.csv')
fatalPoliceShootings = connection.readFromFile('fatal_police_shootings.csv')
drugRelatedDeaths = connection.readFromFile('Accidental_Drug_Related_Deaths__2012-_June_2016.csv')

#-------------------------------------------------------------------------------
#                     Inserting data to tables in database
#-------------------------------------------------------------------------------

insertToOffenses(crimes, cursor, conn)
insertToCities(fatalPoliceShootings, drugRelatedDeaths, cursor, conn)

city_id = getIds('cities', cursor)
offense_id = getIds('offenses', cursor)

insertToMoons(moons, cursor, conn)
insertToCrimes(crimes, offense_id, cursor, conn)
insertToEmergencyCalls(emergencyCalls, cursor, conn)
insertToDrugRelatedDeaths(drugRelatedDeaths, city_id, cursor, conn)
insertToFatalPoliceShootings(fatalPoliceShootings, city_id, cursor, conn)

conn.commit()
cursor.close()
conn.close()
