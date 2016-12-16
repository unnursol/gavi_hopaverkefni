import connection
from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go


cursor, conn = connection.connectToDatabase()
def executeQuery(sqlQuery):
	cursor.execute(sqlQuery)
	results = cursor.fetchall()
	return results

def plot(results, graphName, value1, value2, value3, value4):
	data = [go.Bar(
	    x=[value1, value2, value3, value4],
	    y=[results[0][0], results[0][1], results[0][2], results[0][3]]
	)]
	py.iplot(data, filename=graphName)

def plot(results, graphName, value1, value2, value3, value4, value5):
	data = [go.Bar(
	    x=[value1, value2, value3, value4, value5],
	    y=[results[0][0], results[0][1], results[0][2], results[0][3], results[0][4]]
	)]
	py.iplot(data, filename=graphName)


def plotForMultiples(results, graphName):
	strings = []
	values = []
	for i in results: 
		strings.append(i[0])
		values.append(i[1])
	data = [go.Bar(
	    x=strings,
	    y=values
	)]
	py.iplot(data, filename=graphName)

def subplots(results, graphName):
	strings = []
	firstValues = []
	secondValues = []
	for i in results: 
		strings.append(i[0])
		firstValues.append(i[1])
		secondValues.append(i[1])

	trace1 = go.Bar(
	    x=strings,
	    y=firstValues
	)
	trace2 = go.Bar(
	    x=strings,
	    y=secondValues,
	)

	fig = tools.make_subplots(rows=1, cols=2)

	fig.append_trace(trace1, 1, 1)
	fig.append_trace(trace2, 1, 2)

	fig['layout'].update(height=600, width=600)
	plot_url = py.plot(fig, filename=graphName)