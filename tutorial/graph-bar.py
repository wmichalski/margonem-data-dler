import plotly.plotly as py
import plotly.graph_objs as go
import json

json_file = open('quotes_mil.json')
json_str = json_file.read()
json_data = json.loads(json_str)

wsp_list = []

for element in json_data:
    wsp_list.append(element['wsp'])

wsp_list.sort()

trace1 = go.Bar(
            y=wsp_list
    )

data = [trace1]

py.iplot(data, filename='bar-chart')