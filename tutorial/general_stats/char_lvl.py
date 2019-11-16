import plotly.plotly as py
import plotly.graph_objs as go
import json

json_file = open('char_list.json')
json_str = json_file.read()
json_data = json.loads(json_str)

lvl_dict = {}

for i in range(1000):
    lvl_dict[i] = 0

for account in json_data:
    for char in account['char_list']:
        char_lvl = char[0:-1]
        lvl_dict[int(char_lvl)] += 1

# values will get respective 
lvls = []
values = []

for key, value in lvl_dict.items():
    lvls.append(key)
    values.append(value)

trace1 = go.Bar(
            x=lvls,
            y=values
    )

data = [trace1]

py.iplot(data, filename='char_lvl')