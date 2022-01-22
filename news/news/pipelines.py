# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import pymongo
import sqlite3


class MongodbPipeline(object):
    collection_name = "titles_news"  

    def open_spider(self, spider):
        self.client = pymongo.MongoClient("mongodb+srv://123:123@cluster0.c4y9p.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.db = self.client["Eghtesadnews"]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item) 
        return item


class SQLlitePipeline(object):

    def open_spider(self, spider):
        self.connection = sqlite3.connect("title_news.db")
        self.c = self.connection.cursor()
        try:
            self.c.execute('''
                CREATE TABLE news(
                    subtitle TEXT,
                    title TEXT,
                    title_url TEXT,
                    lead TEXT
                )  
            ''')
            self.connection.commit()
        except sqlite3.OperationalError:
            pass

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        self.c.execute('''
            INSERT INTO news (subtitle,title,title_url,lead) VALUES(?,?,?,?)
         
        ''', (
            item.get('subtitle'),
            item.get('title'),
            item.get('title_url'),
            item.get('lead')
        ))
        self.connection.commit()
        return item

