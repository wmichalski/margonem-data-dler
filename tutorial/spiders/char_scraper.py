import scrapy
import json
import re
import io
import json
from natsort import natsorted, ns
import statistics 

class CharSpider(scrapy.Spider):
    name = "chars"

    start_urls = []

    baseurl = 'https://new.margonem.pl/profile/view,'

    json_file = open('./tutorial/general_stats/id_list_total.json')
    json_str = json_file.read()
    json_data = json.loads(json_str)

    # for i in json_data:
    #     start_urls.append(baseurl+str(i))

    for i in reversed(json_data):
        if i > 9000000:
            start_urls.append(baseurl+str(i))


    # for i in range(1498500,1499523):
    #     start_urls.append(baseurl+str(i))

    def parse(self, response):
        is_public_checker = response.xpath('.//div[@class="character-list"]/h3/text()').get()
        is_public_checker = is_public_checker.strip()

        if is_public_checker != "Światy publiczne":
            return

        chars = response.xpath('.//div[@class="character-list"][1]//ul/*')
        name = response.xpath('//h2/span/text()').get()
        name = name.lstrip()
        name = name.rstrip()

        days = response.xpath('.//div[@class="profile-header-data"][6]//div[@class="value"]/text()').get()
        days = days.replace(' ', '')
        days = int(days)

        posts = response.xpath('.//div[@class="profile-header-data"][1]//div[@class="value"]/text()').get()
        posts = posts.replace(' ', '')
        posts = int(posts)

        page = response.url.split(",")[-1]

        # char includes profession, while lvl does not
        char_list = [] 
        lvl_list = []

        for char in chars:
            lvl = char.xpath('@data-lvl').get()
            prof = char.xpath('input[@class="chprof"]/@value').get()
            char_list.append(lvl + prof)
            lvl_list.append(int(lvl))

        #natsorted(char_list, key=lambda y: y.lower())
        char_list.sort(key = lambda y: int(y[0:-1]), reverse = True)
        
        total = 0
        multiplier = 1.85
        increment = 0.2
        reduce_increment = 0.04
        for char in char_list:
            lvl = char[0:-1]
            if int(lvl) > 20:
                total += (int(lvl)-20)**multiplier
                multiplier += increment
                increment -= reduce_increment
                if increment < 0:
                    increment = 0

        total = total/(days+3.5)

        if posts > 0:
            total *= 0.75


        lvl_list = list(filter(lambda x: x > 10, lvl_list))
        variance = "null"
        if len(lvl_list) > 1:
            variance = statistics.variance(lvl_list)
            variance += 1.7
            variance = variance*(20+days**1.05)/20
            variance = round(variance,2)
            
        
        if total > 300 or variance < 10:
            yield{
                'id': int(page),
                'name': name,
                'days': days,
                'char_list': char_list,
                'total': round(total,2),
                'variance': variance
            }
