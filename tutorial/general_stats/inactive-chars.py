# -*- encoding: utf-8 -*-

import plotly.plotly as py
import plotly.graph_objs as go
import json
import datetime

json_file = open('full_list.json')
json_str = json_file.read()
json_data = json.loads(json_str)
json_file.close()

black_list = [u"Elejlon"]

less_than_month = {}
more_than_month = {}

for element in json_data:
    if element['nick'] in black_list:
        continue

    last_date = datetime.datetime.strptime(element['lastlogin'][7:], '%d.%m.%Y') 
    created_date = datetime.datetime.strptime(element['created'], '%d.%m.%Y') 

    delta = last_date - created_date

    if delta.days > 30:
        if last_date not in more_than_month:
            more_than_month[last_date] = 1
        else:
            more_than_month[last_date] += 1
    else:
        if last_date not in less_than_month:
            less_than_month[last_date] = 1
        else:
            less_than_month[last_date] += 1

# def sorting(L):
#     splitup = L.split('.')
#     return splitup[2], splitup[1], splitup[0]

keys_sorted_more = more_than_month.keys()
keys_sorted_more.sort()

keys_sorted_less = less_than_month.keys()
keys_sorted_less.sort()
# keys_sorted.sort(key=sorting)

# values will get respective 
values_more = []
values_less = []

for key in keys_sorted_more:
    values_more.append(more_than_month[key])

for key in keys_sorted_less:
    values_less.append(less_than_month[key])

# for graph displaying purposes we change our string keys to date
date_list_less = []
date_list_more = []

for key in keys_sorted_more:
    date_list_more.append(key)

for key in keys_sorted_less:
    date_list_less.append(key)

trace1 = go.Bar(
            x=date_list_more,
            y=values_more,
            name='ostatnie logowanie >30 dni od założenia konta'
    )

trace2 = go.Bar(
            x=date_list_less,
            y=values_less,
            name='ostatnie logowanie <=30 dni od założenia konta'
    )

layout = go.Layout(
    barmode='stack',
    title=dict(text=u"Wykres ostatniej aktywności graczy"),
    xaxis=dict(title = "data ostatniego zalogowania"),
    yaxis=dict(title = "ilość graczy"),
    legend=dict(orientation="h"),
)

data = [trace1, trace2]

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='inactive-chars-2')