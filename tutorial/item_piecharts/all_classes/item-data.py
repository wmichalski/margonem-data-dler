import json
import io
import datetime
from collections import OrderedDict

json_file = open('../item-data-source.json')
json_str = json_file.read()
json_data = json.loads(json_str)
json_file.close()

item_dict = {"m": {}, "w": {}, "h": {}, "p": {}, "t": {}, "b": {}}

minlvl = 160
maxlvl = 170
piece_of_eq = 2

select_req = [minlvl, maxlvl, piece_of_eq]

rank_dict = {"c": "[Z]", "u": "[U]", "h": "[H]", "l": "[L]", "p": "[P]"}

for player in json_data:
    for char in player["pub"]:
        prof = char["p"]
        if int(char["l"]) >= minlvl and int(char["l"]) <= maxlvl:
            for item in char["it"]:
                if item["st"] == piece_of_eq:
                    print(item["n"])
                    if item["n"] not in item_dict[prof]:
                        item_dict[prof][item["n"]] = {}
                        item_dict[prof][item["n"]]["freq"] = 1
                        item_dict[prof][item["n"]]["rank"] = rank_dict[item["q"]]
                    else:
                        item_dict[prof][item["n"]]["freq"] += 1

items_descending = {}

for key, value in item_dict.items():
    items_descending[key] = OrderedDict(sorted(item_dict[key].items(), key=lambda v: v[1]["freq"], reverse=True))

with open('filtered-items.json', 'w', encoding='utf8') as outfile:
    json.dump([select_req, items_descending], outfile, ensure_ascii=False)