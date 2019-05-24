import json
import io

json_file = open('bociarze-dict.json')
json_str = json_file.read()
json_bociarze = json.loads(json_str)


print(json_bociarze)

text_file = open("Output.txt", "w")

for key in json_bociarze:
    string = ""
    string = str(json_bociarze[key]).strip('[]')
    string = string.replace('\'', '')
    text_file.write("%s -" % key)    
    text_file.write(" %s\n" % string)

text_file.close()