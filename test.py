

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
                shop_url = shop.xpath('div/div/a/@href')[0]

                if shop_url.strip()[0:4] == 'http':
                    shop_url = shop_url
                else:
                    shop_url = 'https://' + shop_url.strip()[2:]

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

