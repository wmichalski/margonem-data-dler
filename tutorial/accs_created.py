import plotly.plotly as py
import plotly.graph_objs as go
import json
import datetime

json_file = open('quotes_mil.json')
json_str = json_file.read()
json_data = json.loads(json_str)

date_list = []
id_list = []

for element in json_data:
    date = datetime.datetime.strptime(element['created'], '%d.%m.%Y')
    date_list.append(date)
    id_list.append(element['id'])

trace = go.Scattergl(
    y = id_list,
    x = date_list,
    mode = 'markers',
    marker = dict(
        color = '#000000',
        line = dict(width = 1)
    )
)
data = [trace]

py.iplot(data, filename='acc-created')