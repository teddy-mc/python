
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import re
import os
import json
from multiprocessing import Pool
import time

headers = {
    #"Accept":"ext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    #"Accept-Encoding":"gzip, deflate, br",
    #"Accept-Language":"zh-CN,zh;q=0.9",
    #"Cache-Control":"max-age=0",
    #"Host":"maoyan.com",
    #"Proxy-Connection":"keep-alive",
    #"Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    }

#proxies = {
#    "http":"http://47.94.230.42:9999",
#    "https":"https://47.94.230.42:9999",
#}



def get_one_page(url):
    try:
        response = requests.get(url,headers=headers)
        #print (response.encoding)
        response.encoding = 'utf-8'
        #print(response.text)
        if response.status_code == 200 :
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    soup = BeautifulSoup(html, 'lxml')
    urls = soup.find_all(attrs={'class':'gl-item'})
    #print(urls)
    return urls

def second_parse_page(urls):
    for url_1 in urls:
        print(url_1)
        url_1=str(url_1)
        pattern_name = re.compile('<a.*?><em>(.*?)</em><i.*?></i></a></div>',re.S)
        name = re.search(pattern_name,url_1).group(1)
        pattern_price = re.compile('<div class="p-price".*?><i>(.*?)</i>',re.S)
        price = re.search(pattern_price,url_1).group(1)
        #url_name = url_1.text.strip()
        #url_link = 'https://www.aisex.com/bt/'+url_1['href']
        print(name)
        print(price)
        #print(url_link)


def main(offset):
    url = 'https://search.jd.com/Search?keyword=%E5%A5%B6%E7%B2%89&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%A5%B6%E7%B2%89&stock=1&page=' + str(offset)
    model_save_dir = r'C:\Users\a\Documents\python-基础训练\京东'
    model_save_dir = os.path.join(os.getcwd(), model_save_dir)
    if not os.path.exists(model_save_dir):
        os.mkdir(model_save_dir)
    print(url)
    time.sleep(2)
    html = get_one_page(url)
    #print(html)
    urls=parse_one_page(html)
    #print(urls)
    second_parse_page(urls)


if __name__ == '__main__':
    for i in range(1,2):
       main(2*i-1)

    #pool = Pool()
    #pool.map(main,[i*1 for i in range(1,100)])
