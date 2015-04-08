__author__ = 'jovin'
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import MySQLdb

class Snapdeal(BaseSpider):
    name = "snapdeal"
    allowed_domains = ["snapdeal.com"]
    start_urls = ["http://www.snapdeal.com/search?keyword=samsung&santizedKeyword=&catId=0&categoryId=175&suggested=true&vertical=p&noOfResults=80&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=true&foundInAll=false&categoryIdSearched=&cityPageUrl=&url=&utmContent=&catalogID=&dealDetail="]
    def parse(self, response):
        self.conn = MySQLdb.connect(user='root', passwd='2361250', db='test', host='localhost', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()
        i = 0
        price_list = []
        title_list = []
        HtmlXPathSelector(response)
        hxs = HtmlXPathSelector(response)
        links = hxs.select("//div[@class='productWrapper']//div[@class='outerImg']//a/@href").extract()
        images = hxs.select("//div[@class='productWrapper']//div[@class='outerImg']//@hoversrc").extract()
        title = hxs.select("//div[@class='productWrapper']//img/@alt").extract()

        print len(links)