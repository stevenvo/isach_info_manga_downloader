# -*- coding: utf-8 -*-
import scrapy
import urlparse
import re
from isach_info.items import IsachInfoItem

class IsachSpider(scrapy.Spider):
	name = "isach"
	allowed_domains = ["isach.info"]
	start_urls = [
		'http://isach.info/comic.php?list=comic&category=bay_vien_ngoc_rong&order=comic_id&page=3',
		'http://isach.info/comic.php?list=comic&category=bay_vien_ngoc_rong&order=comic_id&page=4',
		'http://isach.info/comic.php?list=comic&category=bay_vien_ngoc_rong&order=comic_id&page=5',
		'http://isach.info/comic.php?list=comic&category=bay_vien_ngoc_rong&order=comic_id&page=6',
	]

	def parse(self, response):
		# self.log('a response from %s just arrived' % response.url)		
		chapter_links = scrapy.Selector(response).xpath('//div[@class="left_list_item"]/a')
		for chapter_link in chapter_links:
			chapter_full_link = urlparse.urljoin(response.url, chapter_link.xpath('@href').extract()[0])
			yield scrapy.Request(chapter_full_link, callback=self.parseComicChapterPage)
			
			
	def parseComicChapterPage(self, response):
		self.log('a response from %s just arrived' % response.url)
		item = IsachInfoItem()
		item['name'] = response.url
		item['image_urls'] = re.findall("\/src='(.*)'",response.body)
		return item


