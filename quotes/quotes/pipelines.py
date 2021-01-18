# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging
import pymongo
import sqlite3

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

class SQLlitePipeline(object):
 
    def open_spider(self, spider):
        self.connection = sqlite3.connect("udemy_tutorial.db")
        self.c = self.connection.cursor()
        try:
            self.c.execute('''
                CREATE TABLE quotes(
                    text TEXT,
                    author TEXT,
                    tags TEXT
                )
            ''')
        
            self.connection.commit()
        except sqlite3.OperationalError:
            pass


    def close_spider(self, spider):
        self.connection.close()
    def process_item(self, item, spider):
        self.c.execute('''
            INSERT INTO quotes (text, author, tags) VALUES (?,?,?)
        ''', (
            item.get('text'),
            item.get('author'), 
            ','.join(item.get('tags'))
            ))
        self.connection.commit()
        return item
