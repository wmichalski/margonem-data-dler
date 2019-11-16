# -*- coding: utf-8 -*-

import json
import io
import datetime
from unidecode import unidecode
from collections import OrderedDict

json_file = open('../item-data-source.json')
json_str = json_file.read()
json_data = json.loads(json_str)
json_file.close()

json_file.close()

player_list = []
name = "Maska złodzieja"

for player in json_data:
    player_dict = {"id": player["id"], "chars": []}
    for char in player["pub"]:
        for item in char["it"]:
            if item["n"] == name:
                player_dict["chars"].append((char["n"], char["l"]+char["p"]))
    if player_dict["chars"]:
        player_list.append(player_dict)

name = name.replace(" ", "-")
name = name.lower()
name = unidecode(name)

with open('bin/' + str(name) + '.json', 'w', encoding='utf8') as outfile:
    outfile.write(
        '[' +
        ',\n'.join(json.dumps(i, ensure_ascii=False) for i in player_list) +
        ']\n')
