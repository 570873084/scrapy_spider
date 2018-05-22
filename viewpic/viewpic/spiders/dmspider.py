# -*- coding: utf-8 -*-
import scrapy
from viewpic.items import ViewpicItem


class DmspiderSpider(scrapy.Spider):
    name = 'dmspider'
    allowed_domains = ['27270.com']
    #url = 'http://www.aitaotu.com/dmtp/list_'
    #num = 1
    #start_urls = [url+str(num)+'.html']
    start_urls= ['http://www.27270.com/tag/866.html']

    def parse(self, response):
        path_list = response.xpath('/html/body/div[2]/div[9]/ul/li')
        for each in path_list:
            item = ViewpicItem()
            item['name'] = each.xpath('./a/span/text()').extract()[0]
            #print('*'*11)
            #print(type(each.xpath('./div[2]/div[1]/span/a/text()').extract()[0]))
            #item['lable']= each.xpath('./div[2]/div[2]/a/text()').extract()[0]
            item['img_link']= each.xpath('./a/img/@src').extract()[0]
            #item['img_url']= each.xpath('./div[2]/div[1]/span/a/@href').extract()[0]
            yield item

