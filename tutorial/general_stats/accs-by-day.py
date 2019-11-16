import plotly.plotly as py
import plotly.graph_objs as go
import json
import datetime

json_file = open('full_list.json')
json_str = json_file.read()
json_data = json.loads(json_str)
json_file.close()

month_dict = {}

for element in json_data:
    if element['created'] not in month_dict:
        month_dict[element['created']] = 1
    else:
        month_dict[element['created']] += 1

def sorting(L):
    splitup = L.split('.')
    return splitup[2], splitup[1], splitup[0]

keys_sorted = month_dict.keys()
keys_sorted.sort(key=sorting)

# values will get respective 
values = []

for key in keys_sorted:
    values.append(month_dict[key])

# for graph displaying purposes we change our string keys to date
date_list = []

for key in keys_sorted:
    date = datetime.datetime.strptime(key, '%d.%m.%Y')
    date_list.append(date)

trace1 = go.Bar(
            x=date_list,
            y=values
    )

data = [trace1]

py.iplot(data, filename='accs-by-day')