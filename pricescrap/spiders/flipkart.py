__author__ = 'jovin'

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from pricescrap.items import Jabong_i
import MySQLdb
from pricescrap.items import Jabong_i

class Flipkart(BaseSpider):
    name = "flipkart"
    allowed_domains = ["flipkart.com"]
    start_urls = ["http://www.flipkart.com/mobiles/pr?p[]=facets.brand%255B%255D%3DMicromax&p[]=facets.operating_system%255B%255D%3DAndroid&sid=tyy%2C4io&ref=8b8a2b4f-53da-487a-9e9a-eb0fd55450cb"]
    def parse(self, response):
        self.conn = MySQLdb.connect(user='root', passwd='2361250', db='test', host='localhost', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()
        i = 0
        price_list = []
        title_list = []
        HtmlXPathSelector(response)
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("//a[@class='fk-display-block']/text()").extract()
        items = hxs.xpath('//span[@class="fk-font-17 fk-bold"]/text()').extract()
        links = hxs.select("//a[@class='fk-display-block']/@href").extract()
        text = hxs.xpath("//ul[@class='pu-usp']//span[@class='text']/text()").extract()
        text_list = [x.encode("utf-8") for x in text]
        text_list = [text_list[x:x+4] for x in range(0, len(text_list),4)]
        images_first =  hxs.xpath("//div[@class='pu-visual-section']/a/img/@src").extract()
        images = hxs.xpath("//div[@class='pu-visual-section']/a/img/@data-src").extract()
        images_first = images_first[0:4]
        images =images_first + images
        links = [x.encode('utf-8') for x in links]
        links = ["http://www.flipkart.com"+x for x in links]
        price_list = [ x.encode('utf-8') for x in items]
        title_list = [x.encode('utf-8') for x in titles]
        title_list = [x.strip() for x in title_list]
        i = 0
        for j in price_list:
            self.cursor.execute("""INSERT INTO Flipkart (title,price,link,image) VALUES (%s,%s,%s,%s)""", (title_list[i]
            ,j,links[i],images[i]))
            self.conn.commit()
            i = i+1
        print images