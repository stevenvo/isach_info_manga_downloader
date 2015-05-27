# -*- coding: utf-8 -*-
import scrapy


class IsachSpider(scrapy.Spider):
    name = "isach"
    allowed_domains = ["isach.info"]
    start_urls = (
        'http://www.isach.info/',
    )

    def parse(self, response):
        pass
