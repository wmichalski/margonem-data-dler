# -*- encoding: utf-8 -*-

import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import *
import json
import datetime
#from datetime import datetime

json_file = open('margomemy.json')
json_str = json_file.read()
json_data = json.loads(json_str)

date_dict = {}

for element in json_data:
    if element['date'] not in date_dict:
        date_dict[element['date']] = 1
    else:
        date_dict[element['date']] += 1

def sorting(L):
    splitup = L.split('.')
    return splitup[0], splitup[1], splitup[2]

keys_sorted = date_dict.keys()
keys_sorted.sort(key=sorting)

# values will get respective 
values = []

for key in keys_sorted:
    values.append(date_dict[key])

date_list = []

for key in keys_sorted:
    date = datetime.datetime.strptime(key, '%Y.%m.%d')
    date_list.append(date)
    
trace = go.Bar(
    y = values,
    x = date_list,
)

layout = Layout(
    title=dict(text=u"Ilość postów napisanych w temacie Margomemy w poszczególne dni"),
    xaxis=dict(title = "data"),
    yaxis=dict(title = "ilość postów"),
)

data = [trace]

fig = Figure(data=data, layout=layout)

py.iplot(fig, filename='posts-by-date-in-margomemy')