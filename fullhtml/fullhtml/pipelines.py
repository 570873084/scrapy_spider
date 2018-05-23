# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql
#导入settings设置
from scrapy.conf import settings


class FullhtmlPipeline(object):
    '''def __init__(self):
        self.filename = open('d:/imgs/context.json','w+',encoding='utf-8')

    def process_item(self, item, spider):
        jsontext = json.dumps(dict(item),ensure_ascii=False) +',\n'
        self.filename.write(jsontext)
        return item

    def close_spider(self,spider):
        self.filename.close()'''
    def __init__(self):
        host = settings['MYSQL_HOST']

        user = settings['MYSQL_USER']
        passwd = settings['MYSQL_PASSWD']

        dbname =settings['MYSQL_DBNAME']

        self.db=pymysql.connect('localhost','root','33655869','img',charset='utf8')
        self.cursor = self.db.cursor()

    def process_item(self,item,spider):
        insert_sql = '''insert into aitaotu2(name,img_link,img_path)values (%s,%s,%s)'''
        self.cursor.execute(insert_sql,(item['name'],item['img_link'],item['img_path']))
        self.db.commit()
        return item


