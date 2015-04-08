__author__ = 'jovin'
__author__ = 'jovin'
import time
from scrapy.spider import BaseSpider
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from scrapy.http import TextResponse
from selenium.webdriver.common.keys import Keys
import MySQLdb
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Snapdeal(BaseSpider):
    name = "flipkart1"
    allowed_domains = ["flipkart.com"]
    start_urls = ["http://www.flipkart.com/mobiles/pr?p[]=facets.brand%255B%255D%3DMotorola&sid=tyy%"
                  "2C4io&otracker=ch_vn_mobile_brand_motorola"]


    def __init__(self):
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference('permissions.default.image', 2)
        self.driver = webdriver.Firefox(firefox_profile=firefox_profile)
    def parse(self, response):
        self.driver.get(response.url)

        copyright = self.driver.find_element_by_class_name('advertisement-tag')
        for i in range(1,2):
            ActionChains(self.driver).move_to_element(copyright).perform()
            time.sleep(15)
        # delay = 3 # seconds
        # try:
        #     WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(self.driver.find_element_by_id('seeMoreProducts')))
        #     print "Page is ready!"
        # except TimeoutException:
        #     print "Loading took too much time!"
        # self.driver.implicitly_wait(25)
        # self.driver.execute_script("window.scrollTo(0,Math.max(document.documentElement.scrollHeight," + "document.body.scrollHeight,document.documentElement.clientHeight));")
        # time.sleep(25)
        # copyright = self.driver.find_element_by_id('seeMoreProducts')
        # # copyright.send_keys(Keys.NULL)
        # ActionChains(self.driver).move_to_element(copyright).perform()
        # # #
        # while not copyright.is_displayed():
        #     copyright = self.driver.find_element_by_id('seeMoreProducts')
        #     time.sleep(20) #to let page content loading
        #     ActionChains(self.driver).move_to_element(copyright).perform()

        response = TextResponse(url=response.url, body=self.driver.page_source, encoding='utf-8')
        titles = response.xpath("//a[@class='fk-display-block']/text()").extract()
        items = response.xpath('//span[@class="fk-font-17 fk-bold"]/text()').extract()
        links = response.xpath("//a[@class='fk-display-block']/@href").extract()
        text = response.xpath("//ul[@class='pu-usp']//span[@class='text']/text()").extract()


        # links = self.driver.find_elements_by_class_name('productWrapper')
        print items