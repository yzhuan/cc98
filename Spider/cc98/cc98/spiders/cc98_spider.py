from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from cc98.items import *

import hashlib

class CC98Spider(CrawlSpider):
    name="cc98"
    allowed_domains=["cc98.org"]
    start_urls=["http://www.cc98.org/hottopic.asp"]
    base_save_dir="data/"
    rules=(Rule(SgmlLinkExtractor(allow=("list.asp")),follow=True),Rule(SgmlLinkExtractor(allow=("dispbbs.asp")),callback="parse_items",follow=False))

    def parse_items(self,response):
        hxs=HtmlXPathSelector(response)
        item=CC98Item()
        item["title"]=hxs.select("//title/text()").extract()
        item["link"]=response.url
        return item
