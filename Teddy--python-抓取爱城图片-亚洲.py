
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import re
import os
import json
from multiprocessing import Pool
import time

headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    #"Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Cache-Control":"max-age=0",
    #"Host":"maoyan.com",
    #"Proxy-Connection":"keep-alive",
    "Upgrade-Insecure-Requests":"1",
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
        response.encoding = 'gbk'
        #print(response.text)
        if response.status_code == 200 :
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    soup = BeautifulSoup(html, 'lxml')
    urls = soup.find_all(attrs={'id':re.compile('a_ajax_.*?')})
    print(urls)
    return urls

def img_download(pics_1,img_save_dir):
    for pic in pics_1.select('img'):
        pic_3 = pic.attrs['src']
        # print(pics)
        # pic_2 =
        # print(pic_2)

        only_file_name = os.path.basename(pic_3)
        save_file_name = os.path.join(img_save_dir, only_file_name)

        if not os.path.exists(save_file_name) or os.path.getsize(save_file_name) == 0:
            print('正在下载：{} ...'.format(save_file_name))
            try:
                r = requests.get(pic_3, timeout=60)
                r.raise_for_status()
                if r.status_code == 200:
                    with open(save_file_name, 'wb') as fw:
                        fw.write(r.content)
            except Exception as e:
                print('Error: ', e)
            time.sleep(0.5)
        else:
            print('文件已存在：{} ...'.format(save_file_name))

def second_parse_page(urls,model_save_dir):
    for url_1 in urls:
        url_name = url_1.text.strip()
        url_link = 'https://www.aisex.com/bt/'+url_1['href']
        print(url_name)
        print(url_link)

        fileName = re.sub('[\/:*?"<>|]', '-', url_name)
        img_save_dir = os.path.join(model_save_dir, fileName)
        if not os.path.exists(img_save_dir):
            os.mkdir(img_save_dir)

        content_1 = requests.get(url_link,timeout=60)
        soup_1 = BeautifulSoup(content_1.text, 'lxml')
        pics = soup_1.find_all(attrs={'id':"read_tpc"})
        pics_1=pics[0]
        print(pics_1)
        #pics = BeautifulSoup(pics.text, 'lxml')
        img_download(pics_1,img_save_dir)



def main(offset):
    url = 'https://www.aisex.com/bt/thread.php?fid=14&page=' + str(offset)
    model_save_dir = r'C:\Users\a\Documents\python-基础训练\aisex'
    model_save_dir = os.path.join(os.getcwd(), model_save_dir)
    if not os.path.exists(model_save_dir):
        os.mkdir(model_save_dir)
    print(url)
    time.sleep(2)
    html = get_one_page(url)
    #print(html)
    urls=parse_one_page(html)
    #print(urls)
    second_parse_page(urls,model_save_dir)


if __name__ == '__main__':


    #for i in range(1,3):
    #   main(i)

    pool = Pool()
    pool.map(main,[i*1 for i in range(1,100)])








