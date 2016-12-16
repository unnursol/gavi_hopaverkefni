import connection
import plotly.plotly as py
import plotly.graph_objs as go


cursor, conn = connection.connectToDatabase()
def emergencyCallsData():
	cursor.execute("select (select count(*) from emergencyCalls where emergencyCalls.time in (select time from moons where moons.phase = 'Full Moon')) as \"Full Moon\", (Select count(*) from emergencyCalls where emergencyCalls.time in (select time from moons where moons.phase = 'New Moon')) as \"New Moon\", (Select count(*) from emergencyCalls where emergencyCalls.time in (select time from moons where moons.phase = 'First Quarter')) as \"First Quarter\", (Select count(*) from emergencyCalls where emergencyCalls.time in (select time from moons where moons.phase = 'Last Quarter')) as \"Last Quarter\";")
	results = cursor.fetchall()
	return results

def crimesData():
	cursor.execute("select (select count(*) from crimes where crimes.time in (select time from moons where moons.phase = 'Full Moon')) as \"Full Moon\", (Select count(*) from crimes where crimes.time in (select time from moons where moons.phase = 'New Moon')) as \"New Moon\", (Select count(*) from crimes where crimes.time in (select time from moons where moons.phase = 'First Quarter')) as \"First Quarter\", (Select count(*) from crimes where crimes.time in (select time from moons where moons.phase = 'Last Quarter')) as \"Last Quarter\";")
	results = cursor.fetchall()
	return results

def fatalPoliceShootingsData():
	cursor.execute("select (select count(*) from fatalpoliceshootings where fatalpoliceshootings.time in (select time from moons where moons.phase = 'Full Moon')) as \"Full Moon\", (Select count(*) from fatalpoliceshootings where fatalpoliceshootings.time in (select time from moons where moons.phase = 'New Moon')) as \"New Moon\", (Select count(*) from fatalpoliceshootings where fatalpoliceshootings.time in (select time from moons where moons.phase = 'First Quarter')) as \"First Quarter\", (Select count(*) from fatalpoliceshootings where fatalpoliceshootings.time in (select time from moons where moons.phase = 'Last Quarter')) as \"Last Quarter\";")
	results = cursor.fetchall()
	return results

def drugDeathsData():
	cursor.execute("select (select count(*) from drugdeaths where drugdeaths.time in (select time from moons where moons.phase = 'Full Moon')) as \"Full Moon\", (Select count(*) from drugdeaths where drugdeaths.time in (select time from moons where moons.phase = 'New Moon')) as \"New Moon\", (Select count(*) from drugdeaths where drugdeaths.time in (select time from moons where moons.phase = 'First Quarter')) as \"First Quarter\", (Select count(*) from drugdeaths where drugdeaths.time in (select time from moons where moons.phase = 'Last Quarter')) as \"Last Quarter\";")
	results = cursor.fetchall()
	return results


results = emergencyCallsData()
data = [go.Bar(
    x=['Full Moon', 'New Moon', 'First Quarter', 'Last Quarter'],
    y=[results[0][0], results[0][1], results[0][2], results[0][3]]
)]
#py.iplot(data, filename='Emergency calls')

results = crimesData()
data = [go.Bar(
    x=['Full Moon', 'New Moon', 'First Quarter', 'Last Quarter'],
    y=[results[0][0], results[0][1], results[0][2], results[0][3]]
)]
#py.iplot(data, filename='Crimes')

results = fatalPoliceShootingsData()
data = [go.Bar(
    x=['Full Moon', 'New Moon', 'First Quarter', 'Last Quarter'],
    y=[results[0][0], results[0][1], results[0][2], results[0][3]]
)]
#py.iplot(data, filename='Fatal police shootings')

results = drugDeathsData()
data = [go.Bar(
    x=['Full Moon', 'New Moon', 'First Quarter', 'Last Quarter'],
    y=[results[0][0], results[0][1], results[0][2], results[0][3]]
)]
py.iplot(data, filename='Drug related deaths')

