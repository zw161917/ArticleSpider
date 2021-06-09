# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import codecs
import json

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ArticlespiderPipeline:
    def process_item(self, item, spider):
        return item

#自定义json文件存储
class  JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open("aeticle.json","a",encoding="utf-8")

    def process_item(self,item,spider):
        lines = json.dumps(dict(item),ensure_ascii=False) +",\n"
        self.file.write(lines)
        return item

    def spider_closed(self,spider):
        self.file.close()


#修改推片下载存储
class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        if "re_images_url" in item:
            for ok, value in results:
                image_file_path = value['path']
            item["re_images_url"] = image_file_path
        return item