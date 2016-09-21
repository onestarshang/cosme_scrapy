# -*- coding: utf-8 -*-

# Scrapy settings for cosme project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'cosme'

SPIDER_MODULES = ['cosme.spiders']
NEWSPIDER_MODULE = 'cosme.spiders'

DOWNLOAD_DELAY = 1.5
COOKIES_ENABLES = False

ITEM_PIPELINES = {
    # 'cosme.pipelines.CosmePipeline': 1,
    # 'cosme.pipelines.ProductPipeline': 1,
    'cosme.pipelines.ProductDetailPipeline': 1,
}
#---mysql config---

HOST, DB, USER, PWD = '127.0.0.1', 'cosme', 'root', 'onestar'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cosme (+http://www.yourdomain.com)'
