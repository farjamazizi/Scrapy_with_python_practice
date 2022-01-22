# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import json


class TitleNewsSpider(CrawlSpider):
    name = 'title_news'
    allowed_domains = ['www.eghtesadnews.com']
    start_urls = ['http://www.eghtesadnews.com/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='views-row']"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//a[@class='global-more']"), callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        yield {
            'subtitle': response.xpath("normalize-space(//div[@class='suptitle']/text())").get(),
            'title': response.xpath("normalize-space(//div[@class='title']/h3/a/text())").get(),
            'title_url': response.urljoin(response.xpath("//div[@class='title']/h3/a/@href").get()),
            'lead': response.xpath("normalize-space(//div[@class='lead']/p/text())").get()
        }

