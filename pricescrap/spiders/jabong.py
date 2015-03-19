from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import MySQLdb

class Jabong(BaseSpider):
    name = "jabong"
    allowed_domains = "jabong.com"
    start_urls = ["http://www.jabong.com/men/shoes/sneakers/?source=topnav_men"]
    def parse(self,response):
        self.conn = MySQLdb.connect(user='root', passwd='2361250', db='test', host='localhost', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()
        hxs = HtmlXPathSelector(response)
        content = hxs.select("//div[@class='box box-bgcolor']")
        price = content.select("//strong[@class='fs16 qa-price']/text()").extract()
        title = content.select(".//span[@class='qa-brandName title mt30 c999 prod-ellipsis']/text()").extract()
        title2 = content.select(".//span[@class='qa-brandTitle fs11 c999 prod-ellipsis']/text()").extract()
        l1 = [elem.strip().split(' ') for elem in title2]
        l2 = [elem.strip().split(' ') for elem in title]
        arr = []
        i = 0
        for l in range(len(l2)):
            text = l2[i]+l1[i]
            arr.append(text)
            i = i+1
        print len(price)