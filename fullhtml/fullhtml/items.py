# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FullhtmlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    # 图片标签
    # lable = scrapy.Field()
    # 图片地址，存储
    img_link = scrapy.Field()
    # 图片网页地址
    # img_url = scrapy.Field()
    #
    img_path = scrapy.Field()