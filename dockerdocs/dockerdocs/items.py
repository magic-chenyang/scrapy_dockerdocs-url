# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DockerdocsItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    data = scrapy.Field()
    description = scrapy.Field()
    texts = scrapy.Field()
    length = scrapy.Field()
    sha1 = scrapy.Field()

