__author__ = 'jovin'
import time
from scrapy.spider import BaseSpider
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from scrapy.http import TextResponse
import MySQLdb

class Snapdeal(BaseSpider):
    name = "snapdeal1"
    allowed_domains = ["snapdeal.com"]
    start_urls = ["http://www.snapdeal.com/search?keyword=nokia&santizedKeyword=nokia&catId=12&categoryId=336&suggested=true&vertical=p&noOfResults=20&clickSrc=searchOnSubCat&lastKeyword=nokia&prodCatId=133&changeBackToAll=true&foundInAll=false&categoryIdSearched=&cityPageUrl=&url=&utmContent=&catalogID=&dealDetail=#bcrumbSearch:nokia|bcrumbLabelId:133"]
    def __init__(self):
        self.driver = webdriver.Firefox()
    def parse(self, response):
        self.driver.get(response.url)
        copyright = self.driver.find_element_by_id('sdFooter')
        ActionChains(self.driver).move_to_element(copyright).perform()

        while not copyright.is_displayed():
            copyright = self.driver.find_element_by_id('sdFooter')
            time.sleep(25) #to let page content loading
            ActionChains(self.driver).move_to_element(copyright).perform()

        response = TextResponse(url=response.url, body=self.driver.page_source, encoding='utf-8')
        links = response.xpath("//a[@class='hit-ss-logger somn-track prodLink hashAdded']/@href").extract()
        price = response.xpath("//span[@id='price']").extract()


        # links = self.driver.find_elements_by_class_name('productWrapper')
        print price

        # images = self.driver.find_element_by_xpath("//div[@class='productWrapper']//div[@class='outerImg']//@hoversrc").text
        # title = self.driver.find_element_by_xpath("//div[@class='productWrapper']//img/@alt").text

