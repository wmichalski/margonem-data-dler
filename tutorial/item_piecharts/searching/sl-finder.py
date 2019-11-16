import json
import io
import datetime
from collections import OrderedDict

json_file = open('../item-data-source.json')
json_str = json_file.read()
json_data = json.loads(json_str)
json_file.close()

player_dict = {}

for player in json_data:
    counter = 0
    for char in player["pub"]:
        for item in char["it"]:
            if item["sl"] == 1:
                counter+=1
    for char in player["priv"]:
        for item in char["it"]:
            if item["sl"] == 1:
                counter+=1
    if counter > 0:
        player_dict[player["n"]] = counter

items_descending = {}

items_descending = OrderedDict(
    sorted(player_dict.items(), key=lambda v: v[1], reverse=True))

with open('filtered-items.json', 'w', encoding='utf8') as outfile:
    json.dump(items_descending, outfile, ensure_ascii=False)
