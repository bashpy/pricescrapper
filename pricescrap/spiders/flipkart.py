__author__ = 'jovin'

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from pricescrap.items import Jabong_i
import MySQLdb
from pricescrap.items import Jabong_i

class Flipkart(BaseSpider):
    name = "flipkart"
    allowed_domains = ["flipkart.com"]
    start_urls = ["http://www.flipkart.com/household/cookware/pots-pans/prestige~brand/pr?sid=r4l%2Cc7t%2Cqov&ref=f143ef7a-e313-461a-aea3-cd120ee9bc60"]
    def parse(self, response):
        self.conn = MySQLdb.connect(user='root', passwd='2361250', db='test', host='localhost', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()
        i = 0
        price_list = []
        title_list = []
        HtmlXPathSelector(response)
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("//a[@class='fk-display-block']/text()").extract()
        products = hxs.select("//div[@id='products']")
        for l in products:
            item = Jabong_i()
            items = []
            items = l.xpath('.//span[@class="fk-font-17 fk-bold"]/text()').extract()
        for j in titles:

            self.cursor.execute("""INSERT INTO data (title,price) VALUES (%s,%s)""", (j,items[i]))
            self.conn.commit()
            i = i+1


