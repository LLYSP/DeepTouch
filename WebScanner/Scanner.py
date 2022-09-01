#-*- codeing = utf-8 -*-
#@TIME : 2022/8/31 18:58
#@File : Scanner
#@Software : PyCharm

import requests
import urllib.request, urllib.error  # 指定URL，获取网页数据

from WebScanner.cms import cmsClasses
from WebScanner.frame import frameClasses
from WebScanner.frontend import frontedClasses
from WebScanner.language import languageClasses
from WebScanner.server import serverClass

urllist=[
    "https://www.douban.com/",
    "https://www.baidu.com/",
    "https://blog.csdn.net/",
    "https://qa.1r1g.com/sf/ask/222752841/",
    "https://www.cnblogs.com/zpchcbd/p/15810575.html",
    "https://github.com/EternalMemory672/smap",
    "https://baike.baidu.com/"
]


def returnHtml(url):
    head = {  # 模拟浏览器头部信息，向豆瓣发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.30"
    }

    req = urllib.request.Request(url=url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

def returnHeader(url):
    header = requests.post(url).headers  # 获取网页
    return header

def getResponse(url):

    #发送数据包到指定url
    html = returnHtml(url)
    # print(html)
    # print("==="*20)
    header = returnHeader(url)
    # print(header)
    return html,header# def frameFinger(content):#框架的正则匹配
#     #使用接收到的content，调用用于多种框架的py文件，分别用于正则匹配。


def cmsFinger(content,header):  # 前端的正则匹配
    classes = cmsClasses.CmsClasses(content,header)
    if classes.Drupal() is not None:
        return classes.Drupal()
    if classes.Joomla() is not None:
        return classes.Joomla()
    if classes.Magento() is not None:
        return classes.Magento()
    if classes.Wordpress() is not None:
        return classes.Wordpress()
    return "Don`t know"

def frontendFinger(content,header):  # 前端的正则匹配
    classes = frontedClasses.FrontendClasses(content,header)
    if classes.Angularjs() is not None:
        return classes.Angularjs()
    if classes.Emberjs() is not None:
        return classes.Emberjs()
    if classes.Jquery() is not None:
        return classes.Jquery()
    if classes.Knockout() is not None:
        return classes.Knockout()
    if classes.Meteorjs() is not None:
        return classes.Meteorjs()
    if classes.Mootools() is not None:
        return classes.Mootools()
    if classes.Prototype() is not None:
        return classes.Prototype()
    if classes.Reactjs() is not None:
        return classes.Reactjs()
    if classes.Vuejs() is not None:
        return classes.Vuejs()
    return "Don`t know"

def serverFinger(content,header):  # 服务的正则匹配
    serverFinder = serverClass.ServerClass(content, header)
    server = serverFinder.findServer()
    if server is not None:
        return server
    return "Don`t know"

def languageFinger(content,header):  # 编程语言的正则匹配
    classes = languageClasses.LanguageClasses(content,header)
    if classes.Asp() is not None:
        return classes.Asp()
    if classes.Java() is not None:
        return classes.Java()
    if classes.Perl() is not None:
        return classes.Perl()
    if classes.Php() is not None:
        return classes.Php()
    if classes.Python() is not None:
        return classes.Python()
    if classes.Ruby() is not None:
        return classes.Ruby()
    return "Don`t know"

def frameFinger(content,header):  # 框架的正则匹配
    classes = frameClasses.FrameClasses(content,header)
    if classes.Cakephp() is not None:
        return classes.Cakephp()
    if classes.Cherrypy() is not None:
        return classes.Cherrypy()
    if classes.Dancer() is not None:
        return classes.Dancer()
    if classes.Django() is not None:
        return classes.Django()
    if classes.Flask() is not None:
        return classes.Flask()
    if classes.Fuelphp() is not None:
        return classes.Fuelphp()
    if classes.Grails() is not None:
        return classes.Grails()
    if classes.Laravel() is not None:
        return classes.Laravel()
    if classes.Mvc() is not None:
        return classes.Mvc()
    if classes.Nette() is not None:
        return classes.Nette()
    if classes.Phalcon() is not None:
        return classes.Phalcon()
    if classes.Rails() is not None:
        return classes.Rails()
    if classes.Symfony() is not None:
        return classes.Symfony()
    if classes.Yii() is not None:
        return classes.Yii()
    if classes.Zend() is not None:
        return classes.Zend()
    return "Don`t know"

def Scanner():
    for url in urllist:
        content,header = getResponse(url)
        print("targe_url:"+url)
        print("="*10+"Scanner Start"+"="*10)

        frame = frameFinger(content,header)
        if frame!="Don`t know":
            print("frame"+">"*10+frame)

        frontend = frontendFinger(content,header)
        if frontend!="Don`t know":
            print("frontend"+">"*10+frontend)

        language = languageFinger(content,header)
        if language!="Don`t know":
            print("language" + ">" * 10 + language)

        server = serverFinger(content,header)
        if server!="Don`t know":
            print("server"+">"*10+server)

        cms = cmsFinger(content,header)
        if cms!="Don`t know":
            print("cms"+">"*10+cms)

if __name__ == '__main__':
    Scanner()