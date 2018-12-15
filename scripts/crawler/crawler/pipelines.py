# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from hazm import *

import json

class CrawlerPipeline(object):
    def open_spider(self, spider):
        self.file = open('corpus.txt', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        sentences=sent_tokenize(item["text"])
        _str = "\n".join(sentences) 
        self.file.write(_str)
        import item

