import connection
import plotly.plotly as py
import plotly.graph_objs as go


cursor, conn = connection.connectToDatabase()
def executeQuery(sqlQuery):
	cursor.execute(sqlQuery)
	results = cursor.fetchall()
	return results

def plot(results, graphName):
	data = [go.Bar(
	    x=['Full Moon', 'New Moon', 'First Quarter', 'Last Quarter'],
	    y=[results[0][0], results[0][1], results[0][2], results[0][3]]
	)]
	py.iplot(data, filename=graphName)


def plotForMultiples(results, graphName):
	strings = []
	values = []
	for i in results: 
		strings.append(i[0])
		values.append(i[1])
	print(strings)
	print(values)
	data = [go.Bar(
	    x=strings,
	    y=values
	)]
	#py.iplot(data, filename=graphName)