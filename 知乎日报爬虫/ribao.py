# -*- coding: UTF-8 -*-

"""
获取知乎日报当日热点文章的url和
title
编码为utf-8的json格式
json文件放置于django框架mysite
静态文件夹中
"""

import json
import urllib2
import time

from bs4 import BeautifulSoup

OUTPUT_POS = '//root//myblog//home//static//home//daily_zhihu.json'
#OUTPUT_POS = '//Users//hongjiayong//Desktop//daily_zhihu.json'
BASIC_URL = 'http://daily.zhihu.com'


if __name__ == '__main__':
    while True:
        print '开始抓取'
        try:
            data = urllib2.urlopen("http://daily.zhihu.com")
        except:
            print '抓取失败'
            exit(0)
        soup = BeautifulSoup(data, 'html.parser')
        list = soup.find_all(attrs={'class': 'link-button'})
        story = []

        for k in list:
            story.append((k['href'], k.find('span').text))

        jsonData = json.loads(json.dumps(story))
        with open(OUTPUT_POS, 'w') as f:
            json.dump(jsonData, f)
            f.close()
            print 'daily_zhihu.json保存完毕' + time.strftime( '%Y-%m-%d %X', time.localtime())
        time.sleep(3600)


