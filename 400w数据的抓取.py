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
import re
from pymongo import MongoClient
from multiprocessing import Pool


client = MongoClient('localhost', 27017) #理解为打开SAS
# 连接test数据库，没有则自动创建
db = client.novel       #理解为建立逻辑库
# 使用zyp集合，没有则自动创建    #理解为建立数据表
my_set = db.novelcontent

def get_Novel_List_Url(url):
    response = requests.get(url,timeout=60) #生成unicode编码，这个是中间编码
    response.encoding = 'gbk'
    html = response.text
    #print(html)
    reg = r'<a target="_blank" title=".*?" href="(.*?)" class="clearfix stitle">(.*?)</a>作者：<a href=".*?">(.*?)</a>'
    urllist=re.findall(reg,html,re.S)
    print('标记1-打印所有“玄幻魔法”标签的首页书籍链接')
    #print(urllist)
    #print('标记2-打印所有“玄幻魔法”标签的首页书籍链接--每一本数据包含变量的个数')
    #print(len(urllist))  # 确定页面中爬取出了多少个链接
    return urllist

def getchapterlist(url):
    #print(url)
    r = requests.get(url,timeout=60)
    r.encoding='gbk'
    html = r.text
    reg = r'<div class="detail">.*?<img src=".*?" class="leftso png_bg"><a href="(.*?)"  class="l mr11">'
    chapterurl = re.findall(reg,html,re.S)[0]
    print('标记4-1---打印每本书的内部链接，就是每本书首页的链接')
    print(chapterurl)
    r = requests.get(chapterurl)
    r.encoding = 'gbk'
    html = r.text
    reg = r'<li><a href="(.*?)" title=".*?字">(.*?)</a></li>'
    chapterlist=re.findall(reg,html) #不需要加上re.S
    #print('标记5')
    #print(chapterlist)
    print('标记4-2--打印每本书所有章节的链接，及章节的标题')
    return chapterlist

def getchaptercontent(url):
    r = requests.get(url,timeout=60)
    r.encoding = 'gbk'
    html = r.text
    reg = r'style5\(\);</script>(.*?)<script type="text/javascript">'
    content = re.findall(reg,html,re.S)
    print('标记5--获取每本书每个章节内的文字')
    #print(content)
    return content


def main(n):
    url='http://www.quanshuwang.com/list/1_'+str(n)+'.html'
    for novel in get_Novel_List_Url(url):
        print('标记3-每本书的链接')
        EveryNovelUrl = novel[0]
        #print(EveryNovelUrl)
        print('标记4--每本书章节的链接')
        charpterlist = getchapterlist(EveryNovelUrl)
        print(charpterlist)
        Everychapterurl=charpterlist
        print('----------------------------')
        print(Everychapterurl)
        #print(getchapterlist(novel[0]))
        for chapter in Everychapterurl:
            print(chapter[0])
            for content in getchaptercontent(chapter[0]):

                my_set.insert_one({"name":novel[1],"charpter":chapter[0],"charptername":chapter[1],"content":getchaptercontent(chapter[0])})

                break

if __name__ == '__main__':


    for i in range(1,2):
        main(i)

    #pool = Pool()
    #pool.map(main,[i*1 for i in range(1,100)])


#mongoexport --db novel --collection novelcontent --type csv --fields name,charpter,charptername,content --out novel.csv