from _plotly_future_ import v4_subplots
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import json


json_file = open('filtered-items.json')
json_str = json_file.read()
json_data = json.loads(json_str)
json_file.close()

select_req = json_data[0]
json_data = json_data[1]

piece_of_eq = ["hełmy", "pierścienie", "naszyjniki", "rękawice", "bronie", "zbroje", "bronie pomocnicze", "buty"]
select_req[2] = piece_of_eq[select_req[2]-1]

labels = {"m": [], "h": [], "w": [], "t": [], "p": [], "b": []}
values = {"m": [], "h": [], "w": [], "t": [], "p": [], "b": []}

# Create subplots, using 'domain' type for pie charts
specs = [[{'type':'domain'}, {'type':'domain'}, {'type':'domain'}], [{'type':'domain'}, {'type':'domain'}, {'type':'domain'}]]
fig = make_subplots(rows=2, cols=3, specs=specs, print_grid=True,  
    subplot_titles=['Wojownik', 'Łowca', 'Tropiciel', 'Paladyn', 'Mag', 'Tancerz ostrzy'])


# Merges the lowest occurencies into a 'other' category to avoid clutter on the graph
for prof, data in json_data.items():
    other = 0
    for key in list(data)[5:]:
        other += data[key]["freq"]
        del data[key]
    json_data[prof]["other"] = {"freq": other, "rank": ""}
# ^^^

# the iterator is for adding spaces at the end - so that each key is unique
# plotly really hates duplicates
it = 0
for prof, data in json_data.items():
    for key, value in data.items():
        labels[prof].append(value["rank"] + " " + key + it*" ")
        values[prof].append(value["freq"])
    it+=1

fig.add_trace(go.Pie(labels=labels["w"], textinfo="value+percent", values=values["w"], name="w", sort = False, 
    marker=dict(colors=['rgb(255,0,0)', 'rgb(210,0,0)', 'rgb(170,0,0)', 'rgb(130,0,0)', 'rgb(90,0,0)', 'gray'])), 1, 1)
fig.add_trace(go.Pie(labels=labels["h"], textinfo="value+percent", values=values["h"], name="h", sort = False, 
    marker=dict(colors=['rgb(0,255,0)', 'rgb(0,210,0)', 'rgb(0,170,0)', 'rgb(0,130,0)', 'rgb(0,90,0)', 'gray'])), 1, 2)
fig.add_trace(go.Pie(labels=labels["t"], textinfo="value+percent", values=values["t"], name="t", sort = False, 
    marker=dict(colors=['rgb(255,0,255)', 'rgb(210,0,210)', 'rgb(170,0,170)', 'rgb(130,0,130)', 'rgb(90,0,90)', 'gray'])), 1, 3)
fig.add_trace(go.Pie(labels=labels["p"], textinfo="value+percent", values=values["p"], name="p", sort = False, 
    marker=dict(colors=['rgb(0,255,255)', 'rgb(0,210,210)', 'rgb(0,170,170)', 'rgb(0,130,130)', 'rgb(0,90,90)', 'gray'])), 2, 1)
fig.add_trace(go.Pie(labels=labels["m"], textinfo="value+percent", values=values["m"], name="m", sort = False, 
    marker=dict(colors=['rgb(150,150,255)', 'rgb(75,75,255)', 'rgb(0,0,240)', 'rgb(0,0,170)', 'rgb(0,0,90)', 'gray'])), 2, 2)
fig.add_trace(go.Pie(labels=labels["b"], textinfo="value+percent", values=values["b"], name="b", sort = False, 
    marker=dict(colors=['rgb(255,255,0)', 'rgb(210,210,0)', 'rgb(170,170,0)', 'rgb(130,130,0)', 'rgb(90,90,0)', 'gray'])), 2, 3)

fig.layout.update(title=str(select_req[0])+"-"+str(select_req[1])+" - " + str(select_req[2]))

fig = go.Figure(fig)

py.iplot(fig, filename='items_all_classes')