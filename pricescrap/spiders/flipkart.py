import scrapy

class flipkart(scrapy.Spider):
    name = "flipkart"
    allowed_domains = ["flipkart.com"]
    start_urls = [
        "http://www.flipkart.com/mens-clothing/t-shirts/pr?p[]=facets.type%255B%255D%3DV-neck&p[]=sort%3Dpopularity&sid=2oq%2Cs9b%2Cj9y&facetOrder[]=type&otracker=clp_mens-clothing-t-shirts_CategoryLinksModule_0-2_catergorylinks_3_VNeck" ]

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            print title, link, desc