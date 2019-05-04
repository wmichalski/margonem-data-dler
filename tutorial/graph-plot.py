import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import *
import json

json_file = open('quotes_mil.json')
json_str = json_file.read()
json_data = json.loads(json_str)

rep_list = []
post_list = []
clr_list = []
nick_list = []

for element in json_data:
    posts = element['posts']
    rep = element['rep']

    rep_list.append(rep)
    post_list.append(posts)
    nick_list.append(element['nick'])

    wsp = rep/(100+pow(posts,0.85))+rep/2000

    clr_s = "#FFFFFF"

    if (wsp < 1.66):
        clr = round((((wsp-1)/0.666666666)*0.2+0.8)*256-1)

        clr_s = "#FFFF" + hex(int(clr))[2:]

    if (wsp < 1):
        clr = round((0.5+0.5*wsp)*256-1)

        clr_s = "#" + hex(int(clr))[2:] +hex(int(clr))[2:] + "00"

    if (wsp < 0):
        clr_s = "#ff0019"

    clr_list.append(clr_s)

trace = go.Scattergl(
    x = post_list,
    y = rep_list,
    mode = 'markers',
    marker = dict(
        color = clr_list,
        line = dict(width = 1),
    ),
    text = nick_list
)
data = [trace]

layout = Layout(
    paper_bgcolor='rgb(0,0,0)',
    plot_bgcolor='rgb(0,0,0)',
    hovermode='closest'
)

fig = Figure(data=data, layout=layout)

py.iplot(fig, filename='compare_webgl')