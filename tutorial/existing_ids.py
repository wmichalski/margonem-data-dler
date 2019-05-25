import json

# getting a list of ids of existing players from data that was earlier scrapped from profiles 

json_file = open('data-3m.json')
json_str = json_file.read()
json_data = json.loads(json_str)

id_list = []

for element in json_data:
    id_list.append(element['id'])

json_id_list = json.dumps(id_list)

with open('id_list.json', 'w') as outfile:
    json.dump(json_id_list, outfile)