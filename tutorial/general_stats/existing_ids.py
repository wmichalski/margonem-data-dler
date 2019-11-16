import json

# getting a list of ids of existing players from data that was earlier scrapped from profiles 

json_file = open('full_list.json')
json_str = json_file.read()
json_data = json.loads(json_str)
json_file.close()

id_list = []

for element in json_data:
    id_list.append(element['id'])

id_list.sort()

with open('id_list_total2.json', 'w') as outfile:
    json.dump(id_list, outfile)