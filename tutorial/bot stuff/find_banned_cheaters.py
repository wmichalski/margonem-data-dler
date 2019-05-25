# -*- encoding: utf-8 -*-

# this script iterates over example10.json (scrapped profiles of ids of cheaters)
# it creates a txt file that shows a list of banned cheaters

import json
import io

json_file = open('example10.json')
json_str = json_file.read()
profile_data = json.loads(json_str)

######
# two loops so that kb players are first on the list:

text_file = open("./bin/zbanowani.txt", "w")
for element in profile_data:
    if element['status'] is not ' ':
        text_file.write("[%s] " % element['status'])
        link = "https://www.margonem.pl/?task=profile&id="+str(element['id'])
        text_file.write("%s - " % link)
        text_file.write("%s" % element['nick'])
        text_file.write("\n")

# end of printing

text_file.close()