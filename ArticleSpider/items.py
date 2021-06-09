# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class JoBoleArticlespiderItem(scrapy.Item):
    re_title = scrapy.Field()
    release_time = scrapy.Field()
    re_url = scrapy.Field()
    url_object_id = scrapy.Field()
    re_author = scrapy.Field()
    re_source = scrapy.Field()
    re_read = scrapy.Field()
    re_text = scrapy.Field()
    re_classify = scrapy.Field()
    re_images_url = scrapy.Field()
    re_recommend = scrapy.Field()