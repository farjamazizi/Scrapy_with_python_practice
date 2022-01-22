# -*- coding: utf-8 -*-
from turtle import title
import scrapy
import logging
from scrapy.shell import inspect_response

# -------------------> Nemone kameltar va sahih  dar poshe news mibashad <-----------------------
class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['www.eghtesadnews.com']
    start_urls = ['https://www.eghtesadnews.com']

    
    
    # def start_requests(self):
    #     yield scrapy.Request(url='https://www.eghtesadnews.com', callback=self.parse, headers={
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    #     })

    
    def parse(self, response):
        for frame in response.xpath("//div[@class='views-row']"):
            yield {
                'subtitle': frame.xpath(".//div[@class='suptitle']/text()").get(),
                'title': frame.xpath(".//div[@class='title']/h3/a/text()").get(),
                'title_url': response.urljoin(frame.xpath(".//div[@class='title']/h3/a/@href").get()),
                'lead': frame.xpath(".//div[@class='lead']/p/text()").get()
            }
        
        
        # next_page = response.xpath("//a[@class='global-more']/@href").get()

        # if next_page:
        #     yield scrapy.Request(url=next_page, callback=self.parse) 
        #     headers={
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
        # })

