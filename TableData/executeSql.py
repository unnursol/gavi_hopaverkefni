import connection
import plotly.plotly as py
import plotly.graph_objs as go
import plotHelperFunctions

"""
def emergencyCallsData():
	cursor.execute("select (select count(time) from emergencyCalls where emergencyCalls.time in (select time from moons where moons.phase = 'Full Moon')) as \"Full Moon\", (Select count(*) from emergencyCalls where emergencyCalls.time in (select time from moons where moons.phase = 'New Moon')) as \"New Moon\", (Select count(*) from emergencyCalls where emergencyCalls.time in (select time from moons where moons.phase = 'First Quarter')) as \"First Quarter\", (Select count(*) from emergencyCalls where emergencyCalls.time in (select time from moons where moons.phase = 'Last Quarter')) as \"Last Quarter\";")
	results = cursor.fetchall()
	return results

def crimesData():
	cursor.execute("select (select count(time) from crimes where crimes.time in (select time from moons where moons.phase = 'Full Moon')) as \"Full Moon\", (Select count(*) from crimes where crimes.time in (select time from moons where moons.phase = 'New Moon')) as \"New Moon\", (Select count(*) from crimes where crimes.time in (select time from moons where moons.phase = 'First Quarter')) as \"First Quarter\", (Select count(*) from crimes where crimes.time in (select time from moons where moons.phase = 'Last Quarter')) as \"Last Quarter\";")
	results = cursor.fetchall()
	return results

def fatalPoliceShootingsData():
	cursor.execute("select (select count(time) from fatalpoliceshootings where fatalpoliceshootings.time in (select time from moons where moons.phase = 'Full Moon')) as \"Full Moon\", (Select count(*) from fatalpoliceshootings where fatalpoliceshootings.time in (select time from moons where moons.phase = 'New Moon')) as \"New Moon\", (Select count(*) from fatalpoliceshootings where fatalpoliceshootings.time in (select time from moons where moons.phase = 'First Quarter')) as \"First Quarter\", (Select count(*) from fatalpoliceshootings where fatalpoliceshootings.time in (select time from moons where moons.phase = 'Last Quarter')) as \"Last Quarter\";")
	results = cursor.fetchall()
	return results

def drugDeathsData():
	cursor.execute("select (select count(time) from drugdeaths where drugdeaths.time in (select time from moons where moons.phase = 'Full Moon')) as \"Full Moon\", (Select count(*) from drugdeaths where drugdeaths.time in (select time from moons where moons.phase = 'New Moon')) as \"New Moon\", (Select count(*) from drugdeaths where drugdeaths.time in (select time from moons where moons.phase = 'First Quarter')) as \"First Quarter\", (Select count(*) from drugdeaths where drugdeaths.time in (select time from moons where moons.phase = 'Last Quarter')) as \"Last Quarter\";")
	results = cursor.fetchall()
	return results

def fullMoonOffensesData():
	cursor.execute("select offense, count(offense_id) from crimes, offenses where offenses.id = crimes.offense_id and crimes.time in (select time from moons where phase like 'Full Moon') group by offenses.offense order by count(offense_id) desc;")
	results = cursor.fetchall()
	return results

def MoonOffensesData():
	cursor.execute("select offense, count(offense_id) from crimes, offenses where offenses.id = crimes.offense_id and crimes.time in (select time from moons where phase like 'Full Moon') group by offenses.offense order by count(offense_id) desc;")
	results = cursor.fetchall()
	return results
#py.iplot(data, filename='Crimes')

"""

results = plotHelperFunctions.executeQuery("select (select count(time) from emergencyCalls where emergencyCalls.time in (select time from moons where moons.phase = 'Full Moon')) as \"Full Moon\", (Select count(*) from emergencyCalls where emergencyCalls.time in (select time from moons where moons.phase = 'New Moon')) as \"New Moon\", (Select count(*) from emergencyCalls where emergencyCalls.time in (select time from moons where moons.phase = 'First Quarter')) as \"First Quarter\", (Select count(*) from emergencyCalls where emergencyCalls.time in (select time from moons where moons.phase = 'Last Quarter')) as \"Last Quarter\";")
plotHelperFunctions.plot(results, 'Emergency calls', 'Full Moon', 'New Moon', 'First Quarter', 'Last Quarter')

results = plotHelperFunctions.executeQuery("select (select count(time) from crimes where crimes.time in (select time from moons where moons.phase = 'Full Moon')) as \"Full Moon\", (Select count(*) from crimes where crimes.time in (select time from moons where moons.phase = 'New Moon')) as \"New Moon\", (Select count(*) from crimes where crimes.time in (select time from moons where moons.phase = 'First Quarter')) as \"First Quarter\", (Select count(*) from crimes where crimes.time in (select time from moons where moons.phase = 'Last Quarter')) as \"Last Quarter\";")
plotHelperFunctions.plot(results, 'Crimes', 'Full Moon', 'New Moon', 'First Quarter', 'Last Quarter')

results = plotHelperFunctions.executeQuery("select (select count(time) from fatalpoliceshootings where fatalpoliceshootings.time in (select time from moons where moons.phase = 'Full Moon')) as \"Full Moon\", (Select count(*) from fatalpoliceshootings where fatalpoliceshootings.time in (select time from moons where moons.phase = 'New Moon')) as \"New Moon\", (Select count(*) from fatalpoliceshootings where fatalpoliceshootings.time in (select time from moons where moons.phase = 'First Quarter')) as \"First Quarter\", (Select count(*) from fatalpoliceshootings where fatalpoliceshootings.time in (select time from moons where moons.phase = 'Last Quarter')) as \"Last Quarter\";")
plotHelperFunctions.plot(results, 'Fatal police shootings', 'Full Moon', 'New Moon', 'First Quarter', 'Last Quarter')

results = plotHelperFunctions.executeQuery("select (select count(time) from drugdeaths where drugdeaths.time in (select time from moons where moons.phase = 'Full Moon')) as \"Full Moon\", (Select count(*) from drugdeaths where drugdeaths.time in (select time from moons where moons.phase = 'New Moon')) as \"New Moon\", (Select count(*) from drugdeaths where drugdeaths.time in (select time from moons where moons.phase = 'First Quarter')) as \"First Quarter\", (Select count(*) from drugdeaths where drugdeaths.time in (select time from moons where moons.phase = 'Last Quarter')) as \"Last Quarter\";")
plotHelperFunctions.plot(results, 'Drug related deaths', 'Full Moon', 'New Moon', 'First Quarter', 'Last Quarter')

#Number of various crimes per phase

results = plotHelperFunctions.executeQuery("select offense, count(offense_id) from crimes, offenses where offenses.id = crimes.offense_id and crimes.time in (select time from moons where phase like 'Full Moon') group by offenses.offense order by count(offense_id) desc;")
plotHelperFunctions.plotForMultiples(results, 'Full moon offenses')

results = plotHelperFunctions.executeQuery("select offense, count(offense_id) from crimes, offenses where offenses.id = crimes.offense_id and crimes.time in (select time from moons where phase like 'New Moon') group by offenses.offense order by count(offense_id) desc;")
plotHelperFunctions.plotForMultiples(results, 'New moon offenses')

results = plotHelperFunctions.executeQuery("select offense, count(offense_id) from crimes, offenses where offenses.id = crimes.offense_id and crimes.time in (select time from moons where phase like 'First Quarter') group by offenses.offense order by count(offense_id) desc;")
plotHelperFunctions.plotForMultiples(results, 'First quarter offenses')

results = plotHelperFunctions.executeQuery("select offense, count(offense_id) from crimes, offenses where offenses.id = crimes.offense_id and crimes.time in (select time from moons where phase like 'Last Quarter') group by offenses.offense order by count(offense_id) desc;")
plotHelperFunctions.plotForMultiples(results, 'Last quarter offenses')

results = plotHelperFunctions.executeQuery("select (select count(sex) from drugdeaths where lower(sex) like 'male' and drugdeaths.time in (select time from moons where moons.phase = 'Full Moon')) as \"Male Deaths on Full moon\", (select count(sex) from drugdeaths where lower(sex) like 'female' and drugdeaths.time in (select time from moons where moons.phase = 'Full Moon')) as \"Female Deaths on Full moon\", (select count(sex) from drugdeaths where lower(sex) like 'male') as \"Male Deaths overall\", (select count(sex) from drugdeaths where lower(sex) like 'female') as \"Female Deaths overall\";")
plotHelperFunctions.plot(results, 'Are there more drugdeaths on full moon', "Male Deaths on Full moon", "Female Deaths on Full moon", "Male Deaths overall", "Female Deaths on overall")

results = plotHelperFunctions.executeQuery("select cause, count(cause) from drugdeaths where time in (select time from moons where phase = 'Full Moon') group by cause order by count(cause) desc;")
plotHelperFunctions.plotForMultiples(results, 'Full moon causes og drugdeaths')

results = plotHelperFunctions.executeQuery("select cause, count(cause) from drugdeaths where time in (select time from moons where phase = 'New Moon') group by cause order by count(cause) desc;")
plotHelperFunctions.plotForMultiples(results, 'New moon causes og drugdeaths')

results = plotHelperFunctions.executeQuery("select cause, count(cause) from drugdeaths where time in (select time from moons where phase = 'First Quarter') group by cause order by count(cause) desc;")
plotHelperFunctions.plotForMultiples(results, 'First quarter causes og drugdeaths')

results = plotHelperFunctions.executeQuery("select race, count(race) from drugdeaths where time in (select time from moons where phase = 'Full Moon') group by race order by count(race) desc;")
plotHelperFunctions.plotForMultiples(results, 'Full moon races og drugdeaths')

results = plotHelperFunctions.executeQuery("select race, count(race) from drugdeaths where time in (select time from moons where phase = 'New Moon') group by race order by count(race) desc;")
plotHelperFunctions.plotForMultiples(results, 'New moon races og drugdeaths')

results = plotHelperFunctions.executeQuery("select race, count(race) from drugdeaths where time in (select time from moons where phase = 'First Quarter') group by race order by count(race) desc;")
plotHelperFunctions.plotForMultiples(results, 'First quarter races og drugdeaths')

results = plotHelperFunctions.executeQuery("select race, count(race) from drugdeaths where time in (select time from moons where phase = 'Last Quarter') group by race order by count(race) desc;")
plotHelperFunctions.plotForMultiples(results, 'Last quarter races og drugdeaths')

results = plotHelperFunctions.executeQuery("select cities.city, count(fatalpoliceshootings.time) from cities, fatalpoliceshootings where cities.id = fatalpoliceshootings.city_id group by cities.city order by count(fatalpoliceshootings.time) desc limit 3;")
plotHelperFunctions.plotForMultiples(results, 'Top cities with police shootings - Full moon')

results = plotHelperFunctions.executeQuery("select cities.city, drugdeath.count as \"Drugdeaths\", policedeaths.count as \"Policedeaths\" from cities, (select count(drugdeaths.time), cities.city from cities, drugdeaths where drugdeaths.city_id = cities.id group by cities.city) as drugdeath full join (select count(fatalpoliceshootings.time), cities.city from cities, fatalpoliceshootings where fatalpoliceshootings.city_id = cities.id group by cities.city) as policedeaths on drugdeath.city = policedeaths.city where cities.city = policedeaths.city or cities.city = drugdeath.city group by cities.city, drugdeath.count, policedeaths.count;")
plotHelperFunctions.subplots(results, 'Top cities with police shootings and drug deaths')

results = plotHelperFunctions.executeQuery("select (select count(offense_id)/186 from crimes where time in (select time from moons where phase like 'New Moon')) as \"New Moon\", (select count(offense_id)/186 from crimes where time in (select time from moons where phase like 'Full Moon')) as \"Full Moon\", (select count(offense_id)/186 from crimes where time in (select time from moons where phase like 'First Quarter')) as \"First Quarter\", (select count(offense_id)/186 from crimes where time in (select time from moons where phase like 'Last Quarter')) as \"Last Quarter\", (select count(offense_id)/5401 from crimes where time not in (select time from moons where phase like 'New Moon')) as \"Normal Day\";")
plotHelperFunctions.plot(results, 'Comparison of crimes between moonphases and normal days', 'New Moon', 'Full Moon', 'First Quarter', 'Last Quarter', 'Other Day' )
