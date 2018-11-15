#导入模块

import requests
import re
from multiprocessing import Pool

# 首先我们写好抓取网页的函数
def get_html(url,tigonger):
    try:
        content = requests.get(url).text
        pattern = re.compile('<a href="(.*?)" class="subject_link thread.*?".*?title=".*?'+tigonger+'.">(.*?)</a>')
        results = re.findall(pattern, content)
        return results
    except:
        return " ERROR "


def get_content(url,tigonger):

    comments = []

    for result in get_html(url,tigonger):
        print(result)
        # 初始化一个字典来存储文章信息
        comment = {}
        # 这里使用一个try except 防止爬虫找不到信息从而停止运行

        url, title = result
        url = 'http://www.btbtt.me/' + url
        print(url)
        try:
            # 开始筛选信息，并保存到字典中
            comment['url'] = url
            comment['title'] = title
            comments.append(comment)
        except:
            print('出了点小问题')

        Out2File(comments, tigonger)

    #return comments


def Out2File(dict,tigonger):
    '''
    将爬取到的文件写入到本地
    保存到当前目录的 TTBT.txt文件中。

    '''
    with open(r'C:\Users\a\Documents\python-基础训练\BTBTT电影\TTBT'+tigonger+'.txt', 'a+') as f:
        for comment in dict:
            f.write('链接:{},电影名字:{},发布者:{}\n'.format(
                comment['url'], comment['title'],tigonger))

        print('当前页面爬取完成')


def main(deep):
    tigonger = 'BTEE'
    base_url = 'http://www.btbtt.me/forum-index-fid-951'
    url_list = []
    # 将所有需要爬去的url存入列表
    #for i in range(1, deep):
    url_list.append(base_url + '-page-' + str(deep)+'.htm')
    print('所有的网页已经下载到本地！ 开始筛选信息。。。。')
    print(url_list)
    # 循环写入所有的数据
    for url_a in url_list:
        print(url_a)
        get_content(url_a, tigonger)
        #content = get_content(url_a,tigonger)
        #print(content)

    print('所有的信息都已经保存完毕！')




if __name__ == '__main__':

    # 设置需要爬取的页码数量
    #deep = 10

    #main(base_url, deep)

    pool = Pool()
    pool.map(main,[i*1 for i in range(1,100)])








