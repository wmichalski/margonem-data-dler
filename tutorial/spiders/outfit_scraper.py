import scrapy
import json
import re
import io

class QuotesSpider(scrapy.Spider):
    name = "outfits"

    start_urls = []

    baseurl = 'https://new.margonem.pl/profile/view,'

    json_file = open('./tutorial/general_stats/id_list_total.json')
    json_str = json_file.read()
    json_data = json.loads(json_str)
    json_file.close()

    last_id_from_json = json_data[-1]

    for i in json_data:
        start_urls.append(baseurl+str(i))

    url_list = []
    

    def parse(self, response):
        chars = response.xpath('.//div[@class="character-list"][1]//ul/*')
        for char in chars:
            chnick = char.xpath('@data-nick').get()
            url = char.xpath('span/@style').get()
            url = url.split('\'')[1][2:]

            if url not in self.url_list:
                self.url_list.append(url)
                yield {chnick:url}
                # i is some mandatory letter because it doesnt work otherwise

        chars = response.xpath('.//div[@class="character-list"][2]//ul/*')
        for char in chars:
            chnick = char.xpath('@data-nick').get()
            url = char.xpath('span/@style').get()
            url = url.split('\'')[1][2:]

            if url not in self.url_list:
                self.url_list.append(url)
                yield {chnick:url}
                # i is some mandatory letter because it doesnt work otherwise

    print(url_list)
    

