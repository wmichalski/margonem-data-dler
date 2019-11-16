# -*- encoding: utf-8 -*-

import json
import io
import datetime

json_file = open('full_list.json')
json_str = json_file.read()
json_data = json.loads(json_str)
json_file.close()

for element in json_data:
    date = datetime.datetime.strptime(element["lastlogin"], '%H:%M, %d.%m.%Y')
    element["ll-datetime"] = date

sorted_list = sorted(json_data, key=lambda k: k['ll-datetime']) 
sorted_ban_list = []

for element in sorted_list:
    del element["ll-datetime"]
    if element["status"] is not " ":
        sorted_ban_list.append(element)

with io.open('ban_list_by_ll.txt', 'w', encoding='utf8') as outfile:
    for i in sorted_ban_list:
        outfile.write("https://www.margonem.pl/?task=profile&id="+ str(i["id"]) + " [" + i["status"] + "] " + i["lastlogin"] + " - " + i["nick"] + "\n")