#-*- coding: utf8 -*-

import subprocess

from cosme.consts import CAT_ID_NAME

cmd = 'scrapy crawl productdetail -a category_id=%s'

for cat_ids in CAT_ID_NAME.keys():
    subprocess.call(cmd % cat_ids, shell=True)
