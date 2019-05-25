# -*- encoding: utf-8 -*-

# aliath_ranking is a huge file with data about each char scrapped from ranking
# char_bots are nicknames from adi wilk's discord
# example3 is data scrapped earlier from profiles of botters found in char_bots file

# script prints: a json file with profiles and characters associacted with those players
#                a list of characters not associated to any player
#                a txt file printing a list of links to profiles, characters, status and whether they are in kb

import json
import io

json_file = open('aliath-ranking.json')
json_str = json_file.read()
aliath_list = json.loads(json_str)

json_file = open('char-bots.json')
json_str = json_file.read()
char_bots = json.loads(json_str)

json_file = open('example3.json')
json_str = json_file.read()
profile_data = json.loads(json_str)

char_bots = list(dict.fromkeys(char_bots))

cheaters_dict = {}

for key, data in aliath_list.items():
    for char in data:
        if char['nick'] in char_bots:
            try:
                if(char['nick'] not in cheaters_dict['https://www.margonem.pl/?task=profile&id=' + key]):
                    cheaters_dict['https://www.margonem.pl/?task=profile&id=' + key].append(char['nick'])
            except KeyError:
                cheaters_dict['https://www.margonem.pl/?task=profile&id=' + key] = [char['nick']]
            char_bots.remove(char['nick'])

with io.open('./bin/bociarze-dict.json', 'w', encoding='utf8') as outfile:
    json.dump(cheaters_dict, outfile, ensure_ascii=False)

with io.open('./bin/not-found-dict.txt', 'w', encoding='utf8') as outfile:
    string = ""
    string = str(char_bots).strip('[]')
    string = string.replace('\'', '')
    outfile.write("%s" % string)

outfile.close()

# create dict with ban and kb values

player_info = {}

print(profile_data)

for element in profile_data:
    player_info[element['id']] = {}
    player_info[element['id']]['ban'] = ""
    player_info[element['id']]['kb'] = ""

    if element['status']=="perm ban":
        player_info[element['id']]['ban'] = "[perm ban]"
    if element['status']=="term ban":
        player_info[element['id']]['ban'] = "[temp ban]"
    if element['kb']==1:
        player_info[element['id']]['kb'] = "[kb]"

######
# two loops so that kb players are first on the list:

text_file = open("./bin/lista-profili.txt", "w")
for key in cheaters_dict:
    id = key.split("=")[-1]
    if player_info[int(id)]['kb']:
        string = ""
        string = str(cheaters_dict[key]).strip('[]')
        string = string.replace('\'', '')
        text_file.write("%s - " % key)
        #text_file.write("%s" % player_info[int(id)]['ban'])
        text_file.write("%s" % player_info[int(id)]['kb'])
        text_file.write(" %s\n" % string)

for key in cheaters_dict:
    id = key.split("=")[-1]
    if not player_info[int(id)]['kb']:
        string = ""
        string = str(cheaters_dict[key]).strip('[]')
        string = string.replace('\'', '')
        text_file.write("%s - " % key)
       # text_file.write("%s" % player_info[int(id)]['ban'])
        text_file.write("%s" % player_info[int(id)]['kb'])
        text_file.write(" %s\n" % string)

# end of printing

text_file.close()