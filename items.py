# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class StockmarketItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    stock_date = Field()
    stock_open = Field()
    stock_high = Field()
    stock_low = Field()
    stock_close = Field()
    stock_volume = Field()
