# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductItem(scrapy.Item):
    prc_id = scrapy.Field()
    prc_bid_name = scrapy.Field()
    prc_name = scrapy.Field()
    prc_url = scrapy.Field()
    prc_rank = scrapy.Field()
    prc_child_cat_id = scrapy.Field()
    pc_child_cat_name = scrapy.Field()
    small_pic_url = scrapy.Field()


class ProductDetailItem(scrapy.Item):
    prc_id = scrapy.Field()
    prc_publish_date = scrapy.Field()
    prc_child_cat_id = scrapy.Field()
    prc_price_jpy = scrapy.Field()
    prc_price_rmb = scrapy.Field()
    prc_info = scrapy.Field()
    large_pic_url = scrapy.Field()
