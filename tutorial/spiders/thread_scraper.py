import scrapy
import re

# this spider downloads data about posts in specific threads

class PostsSpider(scrapy.Spider):
    name = "posts"

    start_urls = []

    baseurl = 'https://www.margonem.pl/?task=forum&show=posts&id=7606&ps='

    for i in range(0,1000):
        start_urls.append(baseurl+str(i))

    def parse(self, response):
        count_name = 0
        count_rep = 0
        for i in range(50):

            id = response.xpath('//td[contains(@class, "puser")]/a/@name')[i].get()
            id = id[4:]

            nick = response.xpath('//td[contains(@class, "puser")]/text()[2]')[i].get()
            if nick != "KONTO USUNIĘTE":
                nick = response.xpath('//div[@class="nickwood"]/h3/text()')[count_name].get()
                count_name+=1

            rep = response.xpath('//div[@class="repgive"]')[i].get()
            if len(rep) > 50:
                rep = response.xpath('//div[@class="repgive"]/span[@ctip="rep"]')[count_rep].get()
                rep = rep.split(' ')[-1]
                rep = rep.split('\t')[0]
                count_rep += 1
            else:
                rep = "0"

            date = response.xpath('//td[contains(@class, "postid")]/text()')[i].get()
            date = date[2:-9]

            yield{
                'id': int(id),    
                'date': date,
                #'nick': nick,
                #'rep': int(rep),
            }

