# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    name = scrapy.Field()
    url = scrapy.Field()
    data = scrapy.Field()
    type = scrapy.Field()
    info = scrapy.Field()
    noteexpress = scrapy.Field()
    notefirst = scrapy.Field()


class ExportItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    id = scrapy.Field()
    export = scrapy.Field()
    type = scrapy.Field()

