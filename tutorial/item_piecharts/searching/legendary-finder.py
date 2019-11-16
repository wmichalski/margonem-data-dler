import json
import io
import datetime
from collections import OrderedDict

json_file = open('../item-data-source.json')
json_str = json_file.read()
json_data = json.loads(json_str)
json_file.close()

item_dict = {}

for player in json_data:
    for char in player["pub"]:
        for item in char["it"]:
            if item["q"] == "l":
                if item["n"] not in item_dict:
                    item_dict[item["n"]] = [0, []]
                item_dict[item["n"]][0] += 1
                item_dict[item["n"]][1].append(char["n"])

items_descending = OrderedDict(sorted(item_dict.items(), key=lambda v: v[1][0], reverse=True))

with open('legendaries_found.json', 'w', encoding='utf8') as outfile:
    outfile.write(
        '[' +
        ',\n'.join(json.dumps(i, ensure_ascii=False) for i in items_descending.items()) +
        ']\n')
