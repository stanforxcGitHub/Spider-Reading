# -*- coding: UTF-8 -*-
"""
加载知乎日报title文件，从而
抓取知乎日报具体文章和配图使
用json格式
"""
import urllib2
import json

import time
from bs4 import BeautifulSoup

BASIC_URL = 'http://daily.zhihu.com'
#INPUT_POS = '//Users//hongjiayong//PycharmProjects//zhihu//daily_zhihu.json'
#OUTPUT_POS = '//Users//hongjiayong//PycharmProjects//zhihu//daily_zhihu_article.json'
INPUT_POS = '//root//myblog//home//static//home//daily_zhihu.json'
OUTPUT_POS = '//root//myblog//home//static//home//daily_zhihu_article.json'

# 深度挖掘文章内容 获取正确的换行
def deepContent(node):
    content = ''
    try:
        if node.children == None:
            if unicode(node.string) != 'None':
                content = content + unicode(node.string)
            return content + '\n'
    except:
        return node.string
    for k in node.children:
        if k.name == 'br' or k.name =='p':
            content += '\n'
        content = content + deepContent(k)
    return content + '\n'

# 获取文章内容
def getContent(id):
    try:
        data = urllib2.urlopen(BASIC_URL + id).read()
        soup = BeautifulSoup(data, "html.parser")
        img = soup.find(attrs={'class': 'img-wrap'})
        src = img.img['src']
        temp = soup.find(attrs={'class':'content'})
        content = ''
        content = content + deepContent(temp)
        print content
        return src, content
    except:
        print "抓取失败"

if __name__ == '__main__':
    while True:
        list = []
        print '开始抓取'
        with open(INPUT_POS, 'r') as f:
            data = json.load(f)
            f.close()
            for k in data:
                list.append(getContent(k[0]))
            jsonData = json.loads(json.dumps(list))
            with open(OUTPUT_POS, 'w') as F:
                json.dump(jsonData, F)
                print 'daily_zhihu_article.json保存完毕' + time.strftime( '%Y-%m-%d %X', time.localtime())

        time.sleep(3600)


