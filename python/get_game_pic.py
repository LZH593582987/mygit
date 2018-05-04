# -*- coding:UTF-8 -*-
import urllib
import re
import os


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getImg(html):
    reg = '<a target="_blank" href="(.+?)" class="proimg">'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    contents = []
    for imgurl in imglist:
        contents.append('http://pic.yxdown.com/' + imgurl)
    return contents


def mkDir(path):
    path = path.strip()
    isExists = os.path.exists(path)
    if not isExists:
        print u"新建了名字叫做", path, u"的文件夹"
        os.makedirs(path)
    else:
        print u"名为", path, u"的文件夹已经创建成功"
    return path


def savePic(imageURL, fileName, path):
    u = urllib.urlopen(imageURL)
    data = u.read()
    filepath = path + "/" + fileName
    f = open(filepath, 'wb')
    f.write(data)
    print u"正在保存一张名称为", fileName, u"的图片"
    f.close()


def dealPic(imgslist, path, pageIndex):
    x = 0
    for imgurl in imgslist:
        html = getHtml(imgurl)
        reg = '"big":"(.+?\.jpg)"'
        imgre = re.compile(reg)
        piclist = re.findall(imgre, html)
        for pic in piclist:
            picname = str(pageIndex) + '_' + str(x)
            savePic(pic, '%s.jpg' % picname, path)
            x += 1


def getPic(pageIndex):
    url = 'http://pic.yxdown.com/list/2_0_' + str(pageIndex) + '.html'
    html = getHtml(url)
    imgslist = getImg(html)
    path = mkDir('game_pics')
    dealPic(imgslist, path, pageIndex)


def getPics(star, end):
    for i in range(star, end + 1):
        getPic(i)


getPics(1, 20)
