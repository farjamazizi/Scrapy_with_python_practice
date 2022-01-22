import scrapy
from scrapy.crawl import CrawlerProcess
from scrapy.utils.project import get_project_settings
from eghtesadnews.spiders.news import NewsSpider


process = CrawlerProcess(settings=get_project_settings())
process.crawl(NewsSpider)
process.start()

