import scrapy
import json
import re
import io


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = []

    baseurl = 'https://www.margonem.pl/?task=profile&id='

    json_file = open('./tutorial/id_list.json')
    json_str = json_file.read()
    json_data = json.loads(json_str)

    for i in json_data:
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

        text = response.xpath('//body').extract()

        #bany
        found_or_no = [m.start() for m in re.finditer('Konto czasowo zablokowane', str(text))]
        if not found_or_no:
            status = " "
        else:
            status = "temp ban"

        found_or_no = [m.start() for m in re.finditer('Konto zablokowane', str(text))]
        if found_or_no:
            status = "perm ban"

        #kb
        found_or_no = [m.start() for m in re.finditer('kb-small', str(text))]
        if not found_or_no:
            kb = 0
        else:
            kb = 1

        found_or_no = [m.start() for m in re.finditer('postacie//crimson', str(text))]
        if found_or_no:
            kb = 1

        yield{
            'id': int(page),
            'posts': int(posts),
            'rep': int(rep),
            'wsp': float(wsp),
            'created': created,   
            'nick': nick,   
            'status': status,
            'kb': kb
        }

