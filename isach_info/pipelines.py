# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request
from PIL import Image
from cStringIO import StringIO
import re

class CustomImagesPipeline(ImagesPipeline):

	#Name download version
	def image_key(self, url):
		org_filename=url.split('/')[-1]
		params = re.findall("(.*)_(\d*)_.*_(\d*).jpg",org_filename) #remember, regex in python return a list of a tuple!!!! This is so stupid		
		new_filename = '{0}-{1}-{2}.jpg'.format(*params[0])
		return '%s' % (new_filename)

	class IsachInfoPipeline(object):
		def process_item(self, item, spider):
			return item





