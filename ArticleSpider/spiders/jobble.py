from urllib import parse
from lxml import etree
import re

import scrapy
from scrapy import Request

class JobbleSpider(scrapy.Spider):
    name = 'jobble'
    allowed_domains = ['kb.cnblogs.com']
    start_urls = ['https://kb.cnblogs.com/']

    def parse(self, response): #
        re_selector = response.xpath('//div[@class="aiticle_item"]/div[@class="message_info"]')
        for post_node in re_selector:
            selector = etree.HTML(post_node.extract())
            re_url = selector.xpath('//div[@class="msg_title"]/p/a/@href')[0]#.extract()
            re_title = selector.xpath('//div[@class="msg_title"]/p/a/text()')[0]
            re_classify = selector.xpath('//div[@class="msg_title"]/p/span/text()')[0]
            re_text = selector.xpath('//div[@class="msg_summary"]/p/text()')[0]
            # print(re_url)
            # print(re_title,re_classify)
            # print(re_text)
            yield Request(url=parse.urljoin(response.url,re_url),meta={"front_image_url":re_classify},callback=self.parse_detail)

        #提取下一页
        # next_url = response.xpath('//div[@id="pager"]/a[last()]/text()').extract_first("")
        # if next_url == "Next >":
        #     next_url = response.xpath('//div[@id="pager"]/a[last()]/@href').extract_first("")
        #     yield Request(url=parse.urljoin(response.url, str(next_url)), callback=self.parse())


    def parse_detail(self,response):
        re_url = response.url
        re_title = response.xpath('//div[@id="left_content_pages"]/h1[@class="contents_header"]/a/text()').extract_first("")
        re_info = response.xpath('//div[@id="left_content_pages"]/div[@class="contents_info"]//text()').extract()
        re_info = ''.join(re_info)
        re_author = re.search(r'作者:(.*?)来源',re_info).group().replace('作者:','').replace('来源','').split()[0]
        re_source = re.search(r'来源:(.*?)发布时间', re_info).group().replace('来源:', '').replace('发布时间', '').split()[0]
        release_time = re.search(r'发布时间:(.*?)阅读', re_info).group().replace('发布时间:', '').replace('阅读', '').split()[0]
        re_read = re.search(r'阅读:(.*?)推荐', re_info).group().replace('阅读:', '').replace('推荐', '').split()[0]
        # re_recommend = re.search(r'推荐:(.*?)原文链接', re_info).group().replace('推荐:', '').replace('原文链接', '').split()[0]
        re_text = response.xpath('//div[@id="ArticleCnt"]/p/text()').extract()
        print(re_url,re_info)
