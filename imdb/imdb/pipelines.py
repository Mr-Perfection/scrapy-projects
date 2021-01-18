# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import logging
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ImdbPipeline:
    @classmethod
    def from_crawler(cls, spider):
        loggin.warning(crawler.settings.get("MONGO_URL"))
    def open_spider(self, spider):
        logging.warning("Spider opened from pipeline")

    def close_spider(self, spider):
        logging.warning("Spider closed from pipeline")

    def process_item(self, item, spider):
        return item
