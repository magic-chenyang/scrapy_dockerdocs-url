# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dockerdocs.items import DockerdocsItem
import html2text, re, redis, os

REDIS_HOST = '59.110.226.204'
REDIS_PORT = '6379'
#Rules_All = "('',)"
#REDIS_KEY = "docs:start_urls"
#Rules_Deny = "('#.*?', 'term*?', 'v1.*?', '.*?md', )"
redis_q = redis.StrictRedis(connection_pool=redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, db=0))

i = 0
#not_data = 0 #统计未采集条数
class DockerdocsSpider(CrawlSpider):
    name = 'dockerdocs_url'
    allowed_domains = ['47.52.73.177']
    start_urls = ['http://47.52.73.177:8888',]

    rules = (
         Rule(LinkExtractor(allow=('',),deny=('#.*?', 'term*?', 'v1.*?', '.*?md',)), callback='parse_item', follow=True),
     )

    def parse_item(self, response):
        global i,not_data
        i += 1 #zhua qu tiao shu
        print(i)
        redis_q.lpush('dockerdocs:yang', response.url)
