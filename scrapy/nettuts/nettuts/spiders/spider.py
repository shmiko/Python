from scrapy.spider import Spider 
from scrapy.selector import Selector 
from nettuts.items import NettutsItem
from scrapy.http import Request
import re

class MySpider(Spider):
	name = "nettuts"
	allowed_domains = ["code.tutsplus.com"]
	start_urls = ["http://code.tutsplus.com/"]

	def parse(self, response):
		sel = Selector(response)
		links = sel.xpath("//nav[@class='pagination']/a/@href").extract()

		# Store already crawled links
		crawledLinks = []

		#Pattern to check proper links
		#linkPattern = re.compile("^(?:ftp|http|https)\:\/\/(?:code)\.(?:tutsplus)\.(?:com)\/(?:posts)\?(?:page)\=\d+\&\w+\=\w+$")
		linkPattern = re.compile("^(?:ftp|http|https)\:\/\/(?:code)\.(?:tutsplus)\.(?:com)\/(?:posts)\?(?:page)\=\d+$")
		#linkPattern = re.compile("^(?:ftp|http|https):\/\/(?:[\w\.\-\+]+:{0,1}[\w\.\-\+]*@)?(?:[a-z0-9\-\.]+)(?::[0-9]+)?(?:\/|\/(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+)|\?(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+))?$")

		for link in links:
			link = "http://code.tutsplus.com" + link # add pre url string

			# If it is proper links and not checked before, yield it to the Spider
			if linkPattern.match(link) and not link in crawledLinks:
				print "Meet\n\n\n"
				crawledLinks.append(link)
				yield Request(link, self.parse) # Will this interrupt current page to be scraped?

		titles = sel.xpath("//a[@class='posts__post-title']/text()").extract()
		for title in titles:
			item = NettutsItem()
			item["title"] = title
			yield item