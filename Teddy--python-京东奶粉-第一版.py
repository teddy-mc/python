import requests
import re
from pymongo import MongoClient
#from multiprocessing import Pool
from requests.exceptions import RequestException

client = MongoClient('localhost', 27017) #理解为打开SAS
# 连接test数据库，没有则自动创建
db = client.JD_naifen       #理解为建立逻辑库
# 使用zyp集合，没有则自动创建    #理解为建立数据表
JD_naifen = db.JD_naifen

def get_JD_naifen_List_Url(url):
    try:
        response = requests.get(url,timeout=60) #生成unicode编码，这个是中间编码
        response.encoding = 'UTF-8'
        if response.status_code == 200 :
             html = response.text
    except RequestException:
        print('error')

    #html = response.text
    #print(html)
    reg = r'<div class="p-img">.*?<a target="_blank".title="(.*?)".href="(.*?)".*?<div class="p-price">.*?<strong class="J_.*?" data-done="1"><em>(.*?)</em><i>(.*?)</i>'
    urllist=re.findall(reg,html,re.S)

    #print(urllist)
    return urllist

def get_JD_naifen_List_detail(url):
    try:
        response = requests.get(url, timeout=60)  # 生成unicode编码，这个是中间编码
        response.encoding = 'gbk'
        if response.status_code == 200:
            html = response.text
    except RequestException:
            print('error')

    #reg = r'<head>.*?<title>(.*?)</title>.*?</head>.*?<ul class="parameter2 p-parameter-list">.*?<li title=.*?>商品名称：(.*?)</li>.*?<li title=.*?>商品编号：(.*?)</li>.*?<li title=.*?>商品毛重：(.*?)</li>.*?<li title=.*?>商品产地：(.*?)</li>.*?<li title=.*?>国产/进口：(.*?)</li>.*?<li title=.*?>净含量：(.*?)</li>.*?<li title=.*?>适用年龄：(.*?)</li>.*?<li title=.*?>包装单位：(.*?)</li>.*?<li title=.*?>配方：(.*?)</li>.*?<li title=.*?>分类：(.*?)</li>.*?<li title=.*?>奶源地：(.*?)</li>.*?<li title=.*?>段位：(.*?)</li>'
    reg = r'<head>.*?<title>(.*?)</title>.*?</head>.*?<ul class="parameter2 p-parameter-list">.*?<li title=.*?>商品名称：(.*?)</li>.*?<li title=.*?>商品编号：(.*?)</li>.*?<li title=.*?>商品毛重：(.*?)</li>'
    name =  re.findall(reg,html,re.S)
    #print(name)
    return name


def main(offset):
    url = 'https://search.jd.com/Search?keyword=%E5%A5%B6%E7%B2%89%20%E4%BA%AC%E4%B8%9C&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%A5%B6%E7%B2%89%20%E4%BA%AC%E4%B8%9C%E8%87%AA&stock=1&page='+ str(offset)+'&s=1&click=0'
    for i in get_JD_naifen_List_Url(url):
        url=i[1]
        #print(i)
        #print(i[0],i[1])
        if url.strip()[0:4] == 'http':
            url_new = url
        else:
            url_new = 'https://' + url.strip()[2:]
        #print(url_new)
        name = get_JD_naifen_List_detail(url_new)
        #print(name)
        print(url_new,i[2],i[3],name)

        JD_naifen.insert_one({"url_new": url_new, "bizhi": i[2], "price": i[3],"name": name})


if __name__ == '__main__':


    for i in range(1,100):
        main(i)