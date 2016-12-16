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
plotHelperFunctions.plot(results, 'Emergency calls')
#py.iplot(data, filename='Emergency calls')
"""
results = plotHelperFunctions.executeQuery("select (select count(time) from crimes where crimes.time in (select time from moons where moons.phase = 'Full Moon')) as \"Full Moon\", (Select count(*) from crimes where crimes.time in (select time from moons where moons.phase = 'New Moon')) as \"New Moon\", (Select count(*) from crimes where crimes.time in (select time from moons where moons.phase = 'First Quarter')) as \"First Quarter\", (Select count(*) from crimes where crimes.time in (select time from moons where moons.phase = 'Last Quarter')) as \"Last Quarter\";")
plotHelperFunctions.plot(results, 'Crimes')

results = plotHelperFunctions.executeQuery("select (select count(time) from fatalpoliceshootings where fatalpoliceshootings.time in (select time from moons where moons.phase = 'Full Moon')) as \"Full Moon\", (Select count(*) from fatalpoliceshootings where fatalpoliceshootings.time in (select time from moons where moons.phase = 'New Moon')) as \"New Moon\", (Select count(*) from fatalpoliceshootings where fatalpoliceshootings.time in (select time from moons where moons.phase = 'First Quarter')) as \"First Quarter\", (Select count(*) from fatalpoliceshootings where fatalpoliceshootings.time in (select time from moons where moons.phase = 'Last Quarter')) as \"Last Quarter\";")
plotHelperFunctions.plot(results, 'Fatal police shootings')
#py.iplot(data, filename='Fatal police shootings')

results = plotHelperFunctions.executeQuery("select (select count(time) from drugdeaths where drugdeaths.time in (select time from moons where moons.phase = 'Full Moon')) as \"Full Moon\", (Select count(*) from drugdeaths where drugdeaths.time in (select time from moons where moons.phase = 'New Moon')) as \"New Moon\", (Select count(*) from drugdeaths where drugdeaths.time in (select time from moons where moons.phase = 'First Quarter')) as \"First Quarter\", (Select count(*) from drugdeaths where drugdeaths.time in (select time from moons where moons.phase = 'Last Quarter')) as \"Last Quarter\";")
plotHelperFunctions.plot(results, 'Drug related deaths')

#py.iplot(data, filename='Drug related deaths')

results = plotHelperFunctions.executeQuery("select offense, count(offense_id) from crimes, offenses where offenses.id = crimes.offense_id and crimes.time in (select time from moons where phase like 'Full Moon') group by offenses.offense order by count(offense_id) desc;")
plotHelperFunctions.plotForMultiples(results, 'Full moon offenses')


results = plotHelperFunctions.executeQuery("select offense, count(offense_id) from crimes, offenses where offenses.id = crimes.offense_id and crimes.time in (select time from moons where phase like 'New Moon') group by offenses.offense order by count(offense_id) desc;")
plotHelperFunctions.plotForMultiples(results, 'New moon offenses')
"""