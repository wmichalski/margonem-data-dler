from _plotly_future_ import v4_subplots
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import json
import math


json_file = open('filtered-items.json')
json_str = json_file.read()
json_data = json.loads(json_str)

select_req = json_data[0]
json_data = json_data[1]

piece_of_eq = ["hełmy", "pierścienie", "naszyjniki", "rękawice", "bronie", "zbroje", "bronie pomocnicze", "buty"]

labels = {x:[] for x in range(1,9)}
values = {x:[] for x in range(1,9)}

# Create subplots, using 'domain' type for pie charts
specs = [[{'type':'domain'}, {'type':'domain'}, {'type':'domain'}, {'type':'domain'}], [{'type':'domain'}, {'type':'domain'}, {'type':'domain'}, {'type':'domain'}]]
fig = make_subplots(rows=2, cols=4, specs=specs, print_grid=True,  
    subplot_titles=['Hełmy', 'Pierścienie', 'Naszyjniki', 'Bronie', 'Zbroje', 'Pomocnicze', 'Buty'])


# Merges the lowest occurencies into a 'other' category to avoid clutter on the graph
for slot, data in json_data.items():
    other = 0
    for key in list(data)[5:]:
        other += data[key]["freq"]
        del data[key]
    json_data[slot]["other"] = {"freq": other, "rank": ""}
# ^^^

# the iterator is for adding spaces at the end - so that each key is unique
# plotly really hates duplicates
for slot, data in json_data.items():
    for key, value in data.items():
        labels[int(slot)].append(value["rank"] + " " + key)
        values[int(slot)].append(value["freq"])

for slot in range(1,9):
    fig.add_trace(go.Pie(labels=labels[slot], textinfo="value+percent", values=values[slot], name=str(slot), sort = False, 
        marker=dict(colors=['rgb(255,0,0)', 'rgb(210,0,0)', 'rgb(170,0,0)', 'rgb(130,0,0)', 'rgb(90,0,0)', 'gray'])), math.ceil(slot/4), 1+(slot-1)%4)


#fig.layout.update(title=str(select_req[0])+"-"+str(select_req[1])+" - " + str(select_req[2]))

fig = go.Figure(fig)


py.iplot(fig, filename='items_single_class')