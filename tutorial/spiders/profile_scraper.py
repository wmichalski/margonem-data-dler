import scrapy
import json


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = []

    baseurl = 'https://www.margonem.pl/?task=profile&id='

    # json_file = open('tutorial/id_list.json')
    # json_str = json_file.read()
    # json_data = json.loads(json_str)
    # json_data2 = json.loads(json_data)

    # for i in json_data2:
    #     start_urls.append(baseurl+str(i))

    for i in range(8000000,9000000):
        start_urls.append(baseurl+str(i))

    def parse(self, response):
        page = response.url.split("=")[-1]

        wsp = response.xpath('//div[@id="inside_bar_left_stats_profile"]/div[7]/div/text()').get()
        wsp = wsp[-len(wsp):-4] # removing unnecessary " [?]"

        posts = response.xpath('//div[@id="inside_bar_left_stats_profile"]/div[5]/div/text()').get()
        
        rep = response.xpath('//div[@id="inside_bar_left_stats_profile"]/div[6]/div/text()').get()

        created = response.xpath('//div[@id="inside_bar_left_stats_profile"]/div[3]/div/text()').get()
        created = created.split(" ")[0]

        nick = response.xpath('//p[@id="nick"]/@tip').get()

        yield{
            'id': int(page),
            'posts': int(posts),
            'rep': int(rep),
            'wsp': float(wsp),
            'created': created,   
            'nick': nick,     
        }

