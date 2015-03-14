__author__ = 'jovin'

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from pricescrap.items import Jabong

from pricescrap.items import Jabong

class Jabong(BaseSpider):
    """Spider for regularly updated livingsocial.com site, San Francisco Page"""
    name = "jabong"
    allowed_domains = ["flipkart.com"]
    start_urls = ["http://www.flipkart.com/household/pressure-cookers-pans/prestige~brand/pr?sid=r4l,u3r&otracker=product_breadCrumbs_Prestige%20Pressure%20Cookers%20%26%20Pans#jumpTo=0|15"]
    def parse(self, response):
        HtmlXPathSelector(response)
        hxs = HtmlXPathSelector(response)
        products = hxs.select("//div[@id='products']")
        print products
        for l in products:
            title = l.xpath('//title/text()').extract()
            price = l.xpath('.//span[@class="fk-bold"]/text()').extract()
            print title,price



