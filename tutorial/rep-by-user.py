# -*- encoding: utf-8 -*-

# it show rep that each user got from the margomemy thread

import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import *
import json
import datetime
import operator
#from datetime import datetime

json_file = open('margomemy.json')
json_str = json_file.read()
json_data = json.loads(json_str)

player_dict = {}

for element in json_data:
    if element['nick'] not in player_dict:
        player_dict[element['nick']] = int(element['rep'])
    else:
        player_dict[element['nick']] += int(element['rep'])

sorted_players = sorted(player_dict.items(), key=operator.itemgetter(1))

players = [i[0] for i in sorted_players]
rep = [i[1] for i in sorted_players]
    
trace = go.Bar(
    y = rep,
    x = players,
)

layout = Layout(
    title=dict(text=u"Ilość zdobytej reputacji (wliczając nz) w Margomemach przez poszczególnych graczy"),
    xaxis=dict(title = "gracz"),
    yaxis=dict(title = "ilość repa"),
)

data = [trace]

fig = Figure(data=data, layout=layout)

py.iplot(fig, filename='spammers-in-margomemy')