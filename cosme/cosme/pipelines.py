# -*- coding: utf-8 -*-

from twisted.enterprise import adbapi
import time
import MySQLdb
import MySQLdb.cursors

from scrapy import log
from settings import HOST, DB, USER, PWD


class CosmePipeline(object):

    def process_item(self, item, spider):
        return item


class ProductPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
            host = HOST,
            db = DB,
            user = USER,
            passwd = PWD,
            cursorclass = MySQLdb.cursors.DictCursor,
            charset = 'utf8',
            use_unicode = True
        )

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)

    # insert the data to databases                 #把数据插入到数据库中
    def _conditional_insert(self, tx, item):
        sql = '''insert into product (prc_id, prc_bid_name, prc_name, prc_url,
                 prc_rank, prc_child_cat_id, pc_child_cat_name, small_pic_url)
                 values (%s, %s, %s, %s, %s, %s, %s, %s);'''
        tx.execute(sql, (item['prc_id'], item['prc_bid_name'], item['prc_name'],
                         item['prc_url'], item['prc_rank'], item['prc_child_cat_id'],
                         item['pc_child_cat_name'], item['small_pic_url']))
    def handle_error(self, e):
        log.err(e)


class ProductDetailPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
            host = HOST,
            db = DB,
            user = USER,
            passwd = PWD,
            cursorclass = MySQLdb.cursors.DictCursor,
            charset = 'utf8',
            use_unicode = True
        )

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)

    # insert the data to databases                 #把数据插入到数据库中
    def _conditional_insert(self, tx, item):
        sql = '''insert into product_detail (prc_id, prc_publish_date, prc_child_cat_id, prc_price_jpy, prc_price_rmb,
                 prc_info, large_pic_url)
                 values (%s, %s, %s, %s, %s, %s, %s);'''
        tx.execute(sql, (item['prc_id'], item['prc_publish_date'], item['prc_child_cat_id'],
                         item['prc_price_jpy'], item['prc_price_rmb'], item['prc_info'],
                         item['large_pic_url']))
    def handle_error(self, e):
        log.err(e)
