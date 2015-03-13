# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PricescrapItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    price = scrapy.Field()

class Jabong(scrapy.Item):
    """Livingsocial container (dictionary-like object) for scraped data"""
    title = scrapy.Field()
    link = scrapy.Field()
    location = scrapy.Field()
    original_price = scrapy.Field()
    price = scrapy.Field()
    end_date = scrapy.Field()