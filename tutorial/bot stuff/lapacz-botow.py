# -*- encoding: utf-8 -*-

import json
import io

json_file = open('aliath-ranking.json')
json_str = json_file.read()
aliath_list = json.loads(json_str)

json_file = open('char-bots.json')
json_str = json_file.read()
char_bots = json.loads(json_str)

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

print(cheaters_dict)

with io.open('./bin/bociarze-dict.json', 'w', encoding='utf8') as outfile:
    json.dump(cheaters_dict, outfile, ensure_ascii=False)

with io.open('./bin/not-found-dict.txt', 'w', encoding='utf8') as outfile:
    string = ""
    string = str(char_bots).strip('[]')
    string = string.replace('\'', '')
    outfile.write("%s" % string)

outfile.close()

text_file = open("./bin/lista-profili.txt", "w")
for key in cheaters_dict:
    string = ""
    string = str(cheaters_dict[key]).strip('[]')
    string = string.replace('\'', '')
    text_file.write("%s -" % key)    
    text_file.write(" %s\n" % string)

text_file.close()