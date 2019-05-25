import json
import io

# getting ids of players from jsons containing links to profiles from aliath's website

json_file = open('fromsite1.json')
json_str = json_file.read()
fs1 = json.loads(json_str)

json_file = open('fromsite2.json')
json_str = json_file.read()
fs2 = json.loads(json_str)

json_file = open('fromsite3.json')
json_str = json_file.read()
fs3 = json.loads(json_str)

id_list = []

for element in fs1:
    id = element[0]
    id = id.split("=")[-1]
    id_list.append(int(id))

for element in fs2:
    id = element[0]
    id = id.split("=")[-1]
    id_list.append(int(id))

for element in fs3:
    id = element['profileId']
    id_list.append(id)

with open('bin/id_list.json', 'w') as outfile:
    json.dump(id_list, outfile)