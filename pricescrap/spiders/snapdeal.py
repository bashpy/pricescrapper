__author__ = 'jovin'
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import MySQLdb

class Snapdeal(BaseSpider):
    name = "snapdeal"
    allowed_domains = ["snapdeal.com"]
    start_urls = ["http://www.snapdeal.com/products/mobiles/?q=Brand%3AMicromax&FID=checkbox_searchable_Brand%20%3A%20Micromax"]
    def parse(self, response):
        self.conn = MySQLdb.connect(user='root', passwd='2361250', db='test', host='localhost', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()
        i = 0
        price_list = []
        title_list = []
        HtmlXPathSelector(response)
        hxs = HtmlXPathSelector(response)
        links = hxs.select("//div[@class='productWrapper']//div[@class='outerImg']//a/@href").extract()
        print links