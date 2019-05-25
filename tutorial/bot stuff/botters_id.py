import json

# creating a list of ids

json_file = open('./bin/bociarze-dict.json')
json_str = json_file.read()
json_data = json.loads(json_str)

id_list = []

for element in json_data:
    id_list.append(int(element.split("=")[-1]))

with open('./bin/id_list.json', 'w') as outfile:
    json.dump(id_list, outfile)