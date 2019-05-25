# -*- encoding: utf-8 -*-

# the graph shows id and date of posts, making a nice graph of activity od users

import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import *
import json
import datetime
from datetime import datetime

json_file = open('posts_since_2007.json')
json_str = json_file.read()
json_data = json.loads(json_str)

date_list = []
id_list = []

for element in json_data:
    date = datetime.strptime(element['date'], '%Y.%m.%d')
    date_list.append(date)
    id_list.append(element['id'])

baddate = datetime.strptime("2013.09.30", '%Y.%m.%d')
middate = datetime.strptime("2014.06.05", '%Y.%m.%d')
gooddate = datetime.strptime("2015.03.05", '%Y.%m.%d')

trace = go.Scattergl(
    y = id_list,
    x = date_list,
    mode = 'markers',
    marker = dict(
        color = '#000000',
        size = 1.5,
    )
)

label = go.Scatter(
    x=[baddate+(gooddate-baddate)/2],
    y=[40000000],
    mode='text',
    text="tamten durny system repa",
    hoverinfo='skip',
    textfont=dict(
        size=13,
        color='#000000'
    )
)

data = [trace, label]

layout = Layout(
    title=dict(text=u"Ilość postów napisanych na forum Margonem od daty"),
    xaxis=dict(title = "data"),
    yaxis=dict(title = "id posta"),
    shapes=[ 
        #    {
        #     'type': 'line',
        #     'x0': baddate,
        #     'x1': baddate,
        #     'y0': 0,
        #     'y1': 45000000,
        #     'line': {
        #         'color': 'rgb(0, 0, 0)',
        #         'width': 1,
        #         'dash': 'dot',
        #     },

        # },

        # {
        #     'type': 'line',
        #     'x0': gooddate,
        #     'x1': gooddate,
        #     'y0': 0,
        #     'y1': 45000000,
        #     'line': {
        #         'color': 'rgb(0, 0, 0)',
        #         'width': 1,
        #         'dash': 'dot',
        #     },

        # },

        {
            'type': 'rect',
            'x0': gooddate,
            'x1': baddate,
            'y0': 0,
            'y1': 45000000,
            'fillcolor': '#d3d3d3',
            'opacity': 0.2,
            'line': {'width':0},

        },
        
        ]
)

fig = Figure(data=data, layout=layout)

py.iplot(fig, filename='posts-by-date')