# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from fullhtml.items import FullhtmlItem


class AitaotuSpider(CrawlSpider):
    name = 'aitaotu'
    allowed_domains = ['www.aitaotu.com']
    start_urls = ['https://www.aitaotu.com/dmtp/list_1.html']

    rules = (
        Rule(LinkExtractor(allow=('/dmtp/list_\d+'),restrict_xpaths=('//div[@id="pageNum"]')),follow=True),
             Rule(LinkExtractor(allow=('/dmtp/\w+/\d+'),restrict_xpaths=('//div[@class="img"]')),callback='parse_item',follow=True),
        Rule(LinkExtractor(allow=('/dmtp/\w+/\d+'),restrict_xpaths=('//div[@class="pages"]')),callback='parse_item',follow=True,)
    )

    def parse_item(self, response):
        #i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        #print(response.body)
        path_list = response.xpath('/html/body/div[3]/div[2]/div[@class="big-pic"]/div[@id="big-pic"]/p/a')
        for each in path_list:
            item = FullhtmlItem()
            item['name'] = each.xpath('./img/@alt').extract()[0]
            # print('*'*11)
            # print(type(each.xpath('./div[2]/div[1]/span/a/text()').extract()[0]))
            # item['lable']= each.xpath('./div[2]/div[2]/a/text()').extract()[0]
            item['img_link'] = each.xpath('./img/@src').extract()[0]
            # item['img_url']= each.xpath('./div[2]/div[1]/span/a/@href').extract()[0]
            item['img_path'] = response.xpath('//h1/text()').extract()[0]
            yield item

