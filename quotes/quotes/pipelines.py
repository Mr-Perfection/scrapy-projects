# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging
import pymongo

class MongodbPipeline(object):
    collection_name = "quotes"
    # @classmethod
    # def from_crawler(cls, crawler):
    #     logging.warning(crawler.settings.get("MONGO_URI"))
    #     return cls

    def open_spider(self, spider):
        self.client = pymongo.MongoClient("mongodb+srv://Stephen:test@cluster0.deck2.mongodb.net/test?retryWrites=true&w=majority")
        self.db = self.client["UDEMY_TUTORIAL"]


    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
        return item
