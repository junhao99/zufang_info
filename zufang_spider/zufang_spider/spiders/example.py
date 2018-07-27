# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['58.com']
    start_urls = ['http://zz.58.com/chuzu']

    def parse(self, response):
        a = response.xpath("//div[@class='des']/h2/a/text()")
        print(a)
        print("12324234234")
