# -*- encoding: utf-8 -*-

import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import *
import json
import datetime

json_file = open('posts2.json')
json_str = json_file.read()
json_data = json.loads(json_str)

date_list = []
id_list = []

for element in json_data:
    date = datetime.datetime.strptime(element['date'], '%Y.%m.%d')
    date_list.append(date)
    id_list.append(element['id'])

trace = go.Scattergl(
    y = id_list,
    x = date_list,
    mode = 'markers',
    marker = dict(
        color = '#000000',
        size = 2,
    )
)
data = [trace]

layout = Layout(
    title=dict(text=u"Ilość postów napisanych na forum Margonem od daty"),
    xaxis=dict(title = "data"),
    yaxis=dict(title = "id posta")
)

fig = Figure(data=data, layout=layout)

py.iplot(fig, filename='posts-by-date')