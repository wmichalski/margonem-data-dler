from _plotly_future_ import v4_subplots
import plotly
import plotly.offline as py
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import json
import math

json_file = open('filtered-items.json')
json_str = json_file.read()
json_data = json.loads(json_str)
json_file.close()

select_req = json_data[0]
json_data = json_data[1]

fichier_html_graphs = open("DASHBOARD.html", 'w')
fichier_html_graphs.write("<html><head><p align=\"center\"><font size=\"6\">" +
                          str(select_req[0]) + "-" + str(select_req[1]) + select_req[2] + "</font></p></head><body>" + "\n")

piece_of_eq = ["hełmy", "pierścienie", "naszyjniki",
               "rękawice", "bronie", "zbroje", "bronie pomocnicze", "buty"]

labels = {x: [] for x in range(1, 9)}
values = {x: [] for x in range(1, 9)}

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

rank_to_color = {"[Z]": "whitesmoke", "[U]": "yellow",
                 "[H]": "cornflowerblue", "[L]": "gold", "[P]": "green"}
colors = {x: [] for x in range(1, 9)}

for slot, data in json_data.items():
    for key in list(data)[:5]:
        colors[int(slot)].append(rank_to_color[data[key]["rank"]])
    colors[int(slot)].append("silver")


for slot in range(1, 9):
    trace = go.Pie(labels=labels[slot], textinfo="value+percent", values=values[int(slot)], name=str(slot), sort=False,
                   marker=dict(colors=colors[slot], line=dict(color='#000000', width=2)))

    data = [trace]
    layout = go.Layout(
        legend=dict(
            orientation="h")
    )

    fig = go.Figure(data=data, layout=layout)

    plotly.offline.plot(fig, filename='bin/Chart_' +
                        str(slot)+'.html', auto_open=False)
    fichier_html_graphs.write("  <object data=\"bin/"+'Chart_'+str(slot) +
                              '.html'+"\" width=\"450\" height=\"400\"></object>"+"\n")


fichier_html_graphs.write("</body></html>")
print("CHECK YOUR DASHBOARD.html In the current directory")
