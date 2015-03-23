# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request
import json
import os.path

class SQLStore(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user='root', passwd='c00ldb1325', db='aj_db', host='192.168.0.172', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

        #log data to json file


def process_item(self, item, spider):

    try:
        print "pipeline"
        print item['headline']
        self.cursor.execute("""INSERT INTO scraped_data (headlines) VALUES (%s,%s)""", ("jovin","vi"))
        self.conn.commit()

    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])

        return item



#log runs into back file
class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('backDataOfScrapes.json', "w")

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write("item === " + line)
        return item