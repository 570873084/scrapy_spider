# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.utils.project import get_project_settings
#scrapy 中
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from scrapy.exceptions import DropItem
import os

class ViewpicPipeline(ImagesPipeline):
    #def process_item(self, item, spider):
        #return item
    #setting文件中一定要设置IMAGES_STORE,不能改成其他变量名,不然程序会自动忽略pipeline
    img_store =get_project_settings().get('IMAGES_STORE')
    def get_media_requests(self, item, spider):
        image_url = item['img_link']
        #print('*'*11)
        #print(image_url)
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, spider):
        image_path = [x['path'] for ok,x in results if ok]

        path1 = '%s%s'%(self.img_store, item['name'])
        print(path1)
        #
        if os.path.exists(path1) == False:
            os.mkdir(path1)
        os.rename(self.img_store + image_path[0], path1 +'/'+ item['name'] + '.jpg')
        #if not image_path:
            #raise DropItem('Item con分类创建文件夹tains no imagine')
        print('正在保存图片',item['name'])
        return item
