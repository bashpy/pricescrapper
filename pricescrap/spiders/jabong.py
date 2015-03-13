__author__ = 'jovin'

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from pricescrap.items import Jabong

from pricescrap.items import Jabong

class Jabong(BaseSpider):
    """Spider for regularly updated livingsocial.com site, San Francisco Page"""
    name = "jabong"
    allowed_domains = ["flipkart.com"]
    start_urls = ["http://www.flipkart.com/prestige-popular-5-l-pressure-cooker/p/itmdvjqqbf9ybfue?pid=PRCDVFAFTHGY2AGA&srno=b_1&ref=e7068d06-4a19-4044-b520-2e4baf20bc90"]
    def parse(self, response):
        HtmlXPathSelector(response)
        hxs = HtmlXPathSelector(response)
        title = response.xpath('//title/text()').extract()
        price = response.xpath('.//span[@class="selling-price omniture-field"]/text()').extract()
        print title,price



