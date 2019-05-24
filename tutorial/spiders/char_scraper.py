import scrapy
import json



class QuotesSpider(scrapy.Spider):
    name = "chars"

    start_urls = []

    baseurl = 'https://www.margonem.pl/?task=profile&id='

    json_file = open('tutorial/id_list.json')
    json_str = json_file.read()
    json_data = json.loads(json_str)
    json_data2 = json.loads(json_data)

    isDone = 0

    for i in json_data2:
        start_urls.append(baseurl+str(i))
        if i > 50000:
            break

    # for i in range(0,30):
    #     start_urls.append(baseurl+str(i))

    def parse(self, response):
        char_list = []
        page = response.url.split("=")[-1]
        nick = response.xpath('//p[@id="nick"]/@tip').get()

        divs = response.xpath('//div[contains(@class, "inside_char_stats")]')

        for div in divs:
            char = div.xpath('.//b[1]/text()').get()
            if char not in char_list:
                char_list.append(char)

        yield{
            'id': int(page),
            'chars': char_list,
            'nick': nick,     
        }

