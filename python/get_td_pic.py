# -*- coding:utf8 -*-
import urllib
import urllib2
import re
import os
import random
import logging


def getContent(url):
    user_agent = '"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"'
    headers = {'User-Agent': user_agent}
    maxTryNum = 10
    for tries in range(maxTryNum):
        try:
            req = urllib2.Request(url, headers=headers)
            html = urllib2.urlopen(req).read()
            break
        except:
            if tries < (maxTryNum - 1):
                continue
            else:
                logging.error("Has tried %d times to access url %s, all failed!", maxTryNum, url)
                break
    return html


def getImg(html):
    reg = '<img class="rg_ic rg_i" data-src="(.+?)" jsaction="load:str.tbn" alt='
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return imglist


def mkDir(path):
    path = path.strip()
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
    return path


def savePic(imageURL, fileName, path):
    u = urllib.urlopen(imageURL)
    data = u.read()
    filepath = path + "/" + fileName
    f = open(filepath, 'wb')
    f.write(data)
    f.close()


def dealPic(imgslist, path):
    x = 1000
    for imgurl in imgslist:
        savePic(imgurl, '%s.jpg' % x, path)
        x += 1


def getPic():
    url = 'https://www.google.com/search?q=%E4%BA%8C%E7%BB%B4%E7%A0%81&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjly-T81evaAhWBwLwKHcysClsQ_AUICigB&biw=2048&bih=1021'
    content = getContent(url)
    imgslist = getImg(content)
    path = mkDir('td_pics')
    dealPic(imgslist, path)


getPic()
