# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsArticle(scrapy.Item):
    title = scrapy.Field()
    text = scrapy.Field()


class Lyrics(scrapy.Item):
    title = scrapy.Field()
    text = scrapy.Field()
