# -*- encoding: utf-8 -*-

import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import *
import numpy as np
import json

json_file = open('data-3m.json')
json_str = json_file.read()
json_data = json.loads(json_str)

rep_list = []
post_list = []
clr_list = []
nick_list = []
wsp_list = []

rep_list2 = []
post_list2 = []
nick_list2 = []

nick_and_rep_list = []

existing_points = {}
black_list = [u"Banownik", u"Sirtuś", u"Sirtek"]

for element in json_data:
    posts = element['posts']
    rep = element['rep']

    # we will remove the points that would overlap
    point = str(posts) + " " + str(rep)

    if point in existing_points:
        continue

    if element['nick'] in black_list:
        continue

    existing_points[point] = 1

    # # # # # # # # #
    # # # # # # # # #

    # elipse shaped area that will show us nicknames 1800 13000
    if (float(pow(rep, 2))/pow(1800, 2) + float(pow(posts, 2))/pow(13000, 2) > 1):
        nick_list2.append(element['nick'])
        rep_list2.append(element['rep'])
        post_list2.append(element['posts'])

    rep_list.append(rep)
    post_list.append(posts)
    wsp_list.append(element['wsp'])
    nick_list.append(element['nick'])

    # wsp below is completely independent from the value in wsp_list
    # we are simply trying to get the exact color instead of the estimated value above
    wsp = rep/(100+pow(posts, 0.85))+float(rep)/2000

    clr_s = "#ffffff"

    if (wsp < 1.66):
        clr = round((((wsp-1)/0.666666666)*0.2+0.8)*256-1)

        clr_s = "#ffff" + hex(int(clr))[2:]

    if (wsp < 1):
        clr = round((0.5+0.5*wsp)*256-1)

        clr_s = "#" + hex(int(clr))[2:] + hex(int(clr))[2:] + "00"

    if (wsp < 0):
        clr_s = "#ff0019"

    clr_list.append(clr_s)
    nick_and_rep_list.append(element['nick']+ "\n" + clr_s)

trace1 = go.Scatter(
    x=post_list,
    y=rep_list,
    mode='markers',
    marker=dict(
        color=clr_list,
        size=1
    ),
    text=nick_and_rep_list,
    name=""
)

trace2 = go.Scatter(
    x=post_list2,
    y=rep_list2,
    mode='text',
    text=nick_list2,
    textposition='top right',
    textfont=dict(
        size=9,
        color='#ffffff'
    )
)

data = [trace1, trace2]

layout = Layout(
    paper_bgcolor='rgb(0,0,0)',
    plot_bgcolor='rgb(0,0,0)',
    hovermode='closest'
)

fig = Figure(data=data, layout=layout)

py.iplot(fig, filename='compare_webgl')
