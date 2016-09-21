# -*- coding: utf-8 -*-

import re

from scrapy import Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

from cosme.items import ProductItem, ProductDetailItem
from cosme.consts import CAT_ID_NAME

from cosme.utils import rundb


class ProductSpider(CrawlSpider):
    name = "product"
    allowed_domains = ["cn.cosme.net"]
    rules = [
        Rule(SgmlLinkExtractor(allow=('/categories/show/'),
                               restrict_xpaths=('//*[@id="contents"]/section[2]/nav[1]/ul/li')),
             callback='parse_item',
             follow=True)
    ]

    def __init__(self, category_id=None, *args, **kwargs):
        super(ProductSpider, self).__init__(*args, **kwargs)
        self.start_urls = [
            'http://cn.cosme.net/categories/show/%s' % category_id
        ]
        self.category_id = category_id

    def parse_item(self, response):
        sel = Selector(response)
        items = []
        products = sel.xpath('//div[@class="prcs jq-prc"]//a[@class="box-text box-text-white"]')
        for product in products:
            item = ProductItem()
            item['prc_url'] = product.xpath('@href').extract()[0].strip('http://')
            item['prc_id'] = item['prc_url'].split('/')[-1]
            item['small_pic_url'] = product.xpath('article/div[1]/img//@src').extract()[0].strip('//')
            item['prc_bid_name'] = product.xpath('article/div[2][@class="prc-bid-name"]/text()').extract()[0].encode('utf8')
            item['prc_name'] = product.xpath('article/div[3][@class="prc-name"]/text()').extract()[0].encode('utf8')
            rank = product.xpath('article/div[4]/span[@class="reviewer-average-count"]/text()').extract()[0]
            item['prc_rank'] = int(float(rank) * 10)
            item['prc_child_cat_id'] = self.category_id
            item['pc_child_cat_name'] = CAT_ID_NAME[self.category_id]
            items.append(item)
        return items


def gen_start_urls(cat_id):
    sql = '''select distinct prc_url from product
             where prc_child_cat_id=%s;''' % cat_id
    rs = rundb(sql)
    return ('http://%s' % r[0] for r in rs)


class ProductDetailSpider(Spider):
    name = "productdetail"
    allowed_domains = ["cn.cosme.net"]

    def __init__(self, category_id=None, *args, **kwargs):
        super(ProductDetailSpider, self).__init__(*args, **kwargs)
        self.category_id = category_id
        self.start_urls = gen_start_urls(self.category_id)

    def parse(self, response):
        sel = Selector(response)
        item = ProductDetailItem()
        item['prc_id'] = int(response.url.split('/')[-1])
        item['large_pic_url'] = sel.xpath('//*[@id="contents"]/section[2]/div/div/div[1]/article/div/img//@src').extract()[0].strip('//')
        infos = sel.xpath('//*[@id="contents"]/section[5]/div[2]/div/p')
        prc_price_jpy, prc_price_rmb = 0, 0
        try:
            _price = infos[5].xpath('text()').extract()[0]
            if ',' in _price:
                pat = re.compile('(\d*,\d+)')
                m = pat.search(_price)
                if m:
                    prc_price_jpy = int(m.group(1).replace(',', ''))
                    prc_price_rmb = int(prc_price_jpy * 0.065)
        except:
            pass
        item['prc_price_jpy'] = prc_price_jpy
        item['prc_price_rmb'] = prc_price_rmb
        prc_publish_date = '0000/00/00'
        try:
            _date = infos[-3].xpath('text()').extract()[0]
            date_pat = re.compile('(\d+/\d+/\d+)')
            m = date_pat.search(_date)
            if m:
                prc_publish_date = _date
        except:
            pass
        item['prc_publish_date'] = prc_publish_date
        item['prc_info'] = infos[-1].xpath('text()').extract()[0]
        item['prc_child_cat_id'] = self.category_id
        return item
