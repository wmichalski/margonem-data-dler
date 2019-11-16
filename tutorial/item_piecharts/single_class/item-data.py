import json
import io
import datetime
from collections import OrderedDict

json_file = open('../item-data-source.json')
json_str = json_file.read()
json_data = json.loads(json_str)

item_dict = {x:{} for x in range(1,9)}

minlvl = 130
maxlvl = 135
req_class = "m"

select_req = [minlvl, maxlvl, req_class]

rank_dict = {"c": "[Z]", "u": "[U]",
             "h": "[H]", "l": "[L]", "p": "[P]"}

for player in json_data:
    for char in player["pub"]:
        prof = char["p"]
        if int(char["l"]) >= minlvl and int(char["l"]) <= maxlvl and prof == req_class:
            for item in char["it"]:
                if item["n"] not in item_dict[item["st"]]:
                    item_dict[item["st"]][item["n"]] = {}
                    item_dict[item["st"]][item["n"]]["freq"] = 1
                    item_dict[item["st"]][item["n"]]["rank"] = rank_dict[item["q"]]
                else:
                    item_dict[item["st"]][item["n"]]["freq"] += 1

items_descending = {}

for key, value in item_dict.items():
    items_descending[key] = OrderedDict(
        sorted(item_dict[key].items(), key=lambda v: v[1]["freq"], reverse=True))

with open('filtered-items.json', 'w', encoding='utf8') as outfile:
    json.dump([select_req, items_descending], outfile, ensure_ascii=False)
