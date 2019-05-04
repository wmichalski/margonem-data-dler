import plotly.plotly as py
import plotly.graph_objs as go
import json

json_file = open('quotes.json')
json_str = json_file.read()
json_data = json.loads(json_str)

id_list = []
rep_list = []
post_list = []

for element in json_data:
    id_list.append(element['id'])
    rep_list.append(element['rep'])
    post_list.append(element['posts'])


trace = go.Scattergl(
    x = post_list,
    y = rep_list,
    mode = 'markers',
    marker = dict(
        color = '#FFBAD2',
        line = dict(width = 1)
    )
)
data = [trace]
py.iplot(data, filename='compare_webgl')