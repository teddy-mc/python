#!/usr/bin/env python
# -*- coding:utf-8-*-
#time : 2018/09/26
#notice: www.quanshuwang.com的网站编码是:gbk
# pycharm默认的编码是utf-8，而网页的编码是gbk，所以需要把pycharm的默认编码临时设置为gbk
# requests的到的结果有两种一种是text，一种是unicode，我们可以针对unicode进行重新编码，编码为gbk（gbk》unicode》utf8）
# decode:解码，把一种编码转换成unicode  || encode：编码：把unicode转换成一种编码
#version :1.0
#_author_:Teddy
#

import requests
#import re
from pymongo import MongoClient
#from multiprocessing import Pool
from requests.exceptions import RequestException
from lxml import etree

def requests_html(url):
    try:
        response = requests.get(url,headers=headers,timeout=60)  # 生成unicode编码，这个是中间编码
        response.encoding = 'UTF-8'
        if response.status_code == 200:
            selector = etree.HTML(response.text)
            shop_list=selector.xpath('//ul[@class="gl-warp clearfix"]/li')
            for shop in shop_list:
                shop_url = shop.xpath('@data-sku')[0]
                print(shop_url)
            return
    except RequestException:
        print('error')
        return None

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    urls = ['https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page={}&s=1&click=0'.format(i) for i in range(1,10,2)]
    #print(urls)
    for url in urls:
        print(url)
        requests_html(url)
        break

