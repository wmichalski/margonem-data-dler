import json

json_file = open('../item-data-source.json')
json_str = json_file.read()
json_data = json.loads(json_str)
json_file.close()

min_lvl = 75

suspiciousNicks = []

for player in json_data:
    for char in player["pub"]:
        if int(char["l"]) >= min_lvl:
            counter = 0
            for item in char["it"]:
                if item['q'] == "c":
                    counter+=1
            if counter >= 7:
                suspiciousNicks.append(player["n"])
                break

final_list = []

for player in json_data:
    if player["n"] in suspiciousNicks:
        pub_nicks=[]
        priv_chars=[]
        for char in player["pub"]:
            pub_nicks.append(char["l"]+char["p"])
        for char in player["priv"]:
            priv_chars.append(char["l"]+char["p"])
        final_list.append({"id": player["id"], "nick": player["n"], "chars": {"pub": pub_nicks, "priv":priv_chars}})


with open('bin/file.json', 'w', encoding='utf8') as fp:
    fp.write(
        '[' +
        ',\n'.join(json.dumps(i, ensure_ascii=False) for i in final_list) +
        ']\n')

                