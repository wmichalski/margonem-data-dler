import scrapy
import json
import re
import io
import json
import html

class ItemSpider(scrapy.Spider):
    name = "items"

    start_urls = []

    baseurl = 'https://new.margonem.pl/profile/view,'

    json_file = open('./tutorial/general_stats/id_list_total.json')
    json_str = json_file.read()
    json_data = json.loads(json_str)

    last_id_from_json = json_data[-1]

    for i in json_data:
        start_urls.append(baseurl+str(i))

    for i in range(last_id_from_json+1,9110000):
        start_urls.append(baseurl+str(i))

    def parse(self, response):
        chars = response.xpath('.//div[@class="character-list"][1]//ul/*')
        name = response.xpath('//h2/span/text()').get()
        name = name.lstrip()
        name = name.rstrip()

        char_list = []

        for char in chars:
            chnick = char.xpath('@data-nick').get()
            lvl = char.xpath('@data-lvl').get()
            prof = char.xpath('input[@class="chprof"]/@value').get()
            htmlstring = char.xpath('input[@class="chitems"]/@value').get()
            jsonstring = html.unescape(htmlstring)
            jsonitems_uncleaned = json.loads(jsonstring)

            jsonitems = []
            
            for item in jsonitems_uncleaned:
                del item["pr"]
                del item["cl"]
                del item["hid"]
                del item["id"]
                del item["icon"]

                item["rank"] = "common"
                if ";heroic" in item["stat"]:
                    item["rank"] = "heroic"
                if ";unique" in item["stat"]:
                    item["rank"] = "unique"
                if ";legendary" in item["stat"]:
                    item["rank"] = "legendary"
                if ";upgraded" in item["stat"]:
                    item["rank"] = "upgraded"

                item["premium"] = 0
                if item["rank"] == "upgraded" or "upg=" in item["stat"] or "lowreq=" in item["stat"]:
                    item["premium"] = 1
                    
                del item["stat"]

                if item["st"] <= 8:
                    jsonitems.append(item)


            # "st" - respective pieces of gear, with 9 being an itemslot, and 10 being a blessing
            # upgraded - a parameter of premium items
            # ;upg= - a parameter of percentage based upgraded items

            char = {
                'chnick': chnick,
                'lvl': lvl,
                'prof': prof,
                'jsonitems': jsonitems
            }

            char_list.append(char)

        yield{
                'name': name,
                'char_list': char_list

        }

