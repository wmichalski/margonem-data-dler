import scrapy
import json
import re
import io
import json
import html

class ItemSpider(scrapy.Spider):
    name = "items2"

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
        is_public_checker = response.xpath('.//div[@class="character-list"]/h3/text()').get()
        is_public_checker = is_public_checker.strip()

        public = []
        private = []

        acc_id = int(response.url.split(",")[-1])

        if is_public_checker == "Światy publiczne":
            chars = response.xpath('.//div[@class="character-list"][1]//ul/*')
            name = response.xpath('//h2/span/text()').get()
            name = name.lstrip()
            name = name.rstrip()

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

                    item["n"] = item["name"]
                    del item["name"]

                    item["q"] = "c"
                    if ";heroic" in item["stat"]:
                        item["q"] = "h"
                    if ";unique" in item["stat"]:
                        item["q"] = "u"
                    if ";legendary" in item["stat"]:
                        item["q"] = "l"
                    if ";upgraded" in item["stat"]:
                        item["q"] = "p"

                    item["sl"] = 0
                    if item["q"] == "p" or "upg=" in item["stat"] or "lowreq=" in item["stat"]:
                        item["sl"] = 1
                        
                    del item["stat"]

                    if item["st"] <= 8:
                        jsonitems.append(item)


                # "st" - respective pieces of gear, with 9 being an itemslot, and 10 being a blessing
                # upgraded - a parameter of premium items
                # ;upg= - a parameter of percentage based upgraded items

                char = {
                    'n': chnick,
                    'l': lvl,
                    'p': prof,
                    'it': jsonitems
                }

                public.append(char)

            # now the priv charaters
            chars = response.xpath('.//div[@class="character-list"][2]//ul/*')
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

                    item["n"] = item["name"]
                    del item["name"]

                    item["q"] = "c"
                    if ";heroic" in item["stat"]:
                        item["q"] = "h"
                    if ";unique" in item["stat"]:
                        item["q"] = "u"
                    if ";legendary" in item["stat"]:
                        item["q"] = "l"
                    if ";upgraded" in item["stat"]:
                        item["q"] = "p"

                    item["sl"] = 0
                    if item["q"] == "upgraded" or "upg=" in item["stat"] or "lowreq=" in item["stat"]:
                        item["sl"] = 1
                        
                    del item["stat"]

                    if item["st"] <= 8:
                        jsonitems.append(item)


                # "st" - respective pieces of gear, with 9 being an itemslot, and 10 being a blessing
                # upgraded - a parameter of premium items
                # ;upg= - a parameter of percentage based upgraded items

                char = {
                    'n': chnick,
                    'l': lvl,
                    'p': prof,
                    'it': jsonitems
                }

                private.append(char)
        else:
            chars = response.xpath('.//div[@class="character-list"][1]//ul/*')
            name = response.xpath('//h2/span/text()').get()
            name = name.lstrip()
            name = name.rstrip()

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

                    item["n"] = item["name"]
                    del item["name"]

                    item["q"] = "c"
                    if ";heroic" in item["stat"]:
                        item["q"] = "h"
                    if ";unique" in item["stat"]:
                        item["q"] = "u"
                    if ";legendary" in item["stat"]:
                        item["q"] = "l"
                    if ";upgraded" in item["stat"]:
                        item["q"] = "p"

                    item["sl"] = 0
                    if item["q"] == "upgraded" or "upg=" in item["stat"] or "lowreq=" in item["stat"]:
                        item["sl"] = 1
                        
                    del item["stat"]

                    if item["st"] <= 8:
                        jsonitems.append(item)


                # "st" - respective pieces of gear, with 9 being an itemslot, and 10 being a blessing
                # upgraded - a parameter of premium items
                # ;upg= - a parameter of percentage based upgraded items

                char = {
                    'c': chnick,
                    'l': lvl,
                    'p': prof,
                    'it': jsonitems
                }

                private.append(char)

        yield{
                'n': name,
                'id': acc_id,
                'pub': public,
                'priv': private

        }

