# -*- codeing = utf-8 -*-
# @TIME : 2022/8/31 18:58
# @File : Scanner
# @Software : PyCharm

import requests
import urllib.request, urllib.error  # 指定URL，获取网页数据

from WebScanner.cms import cmsClasses
from WebScanner.frame import frameClasses
from WebScanner.frontend import frontedClasses
from WebScanner.language import languageClasses
from WebScanner.server import serverClass
from WebScanner.system import systemClasses
from WebScanner.waf import wafClasses

urllist = [
    "https://www.douban.com/",
    "https://www.baidu.com/",
    "https://blog.csdn.net/",
    "https://qa.1r1g.com/sf/ask/222752841/",
    # "https://www.cnblogs.com/zpchcbd/p/15810575.html",
    # "https://github.com/EternalMemory672/smap",
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
    # 发送数据包到指定url
    html = returnHtml(url)
    # print(html)
    # print("==="*20)
    header = returnHeader(url)
    # print(header)
    return html, header  # def frameFinger(content):#框架的正则匹配


#     #使用接收到的content，调用用于多种框架的py文件，分别用于正则匹配。


def cmsFinger(content, header):  # 前端的正则匹配
    classes = cmsClasses.CmsClasses(content, header)
    if classes.Drupal() is not None:
        return classes.Drupal()
    if classes.Joomla() is not None:
        return classes.Joomla()
    if classes.Magento() is not None:
        return classes.Magento()
    if classes.Wordpress() is not None:
        return classes.Wordpress()
    return "\'\'"


def frameFinger(content, header):  # 框架的正则匹配
    classes = frameClasses.FrameClasses(content, header)
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
    return "\'\'"


def frontendFinger(content, header):  # 前端的正则匹配
    classes = frontedClasses.FrontendClasses(content, header)
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
    return "\'\'"


def languageFinger(content, header):  # 编程语言的正则匹配
    classes = languageClasses.LanguageClasses(content, header)
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
    return "\'\'"


def serverFinger(content, header):  # 服务的正则匹配
    serverFinder = serverClass.ServerClass(content, header)
    server = serverFinder.findServer()
    if server is not None:
        return server
    return "\'\'"


def systemFinger(content, header):
    classes = systemClasses.SystemClasses(content, header)
    if classes.Bsd() is not None:
        return classes.Bsd()
    if classes.Linux() is not None:
        return classes.Linux()
    if classes.Mac() is not None:
        return classes.Mac()
    if classes.Solaris() is not None:
        return classes.Solaris()
    if classes.Unix() is not None:
        return classes.Unix()
    if classes.Windows() is not None:
        return classes.Windows()
    return "\'\'"


def wafFinger(content, header):
    classes = wafClasses.WafClasses(content, header)
    if classes.Airlock() is not None:
        return classes.Airlock()
    if classes.Anquanboa() is not None:
        return classes.Anquanboa()
    if classes.Aws() is not None:
        return classes.Aws()
    if classes.Baidu() is not None:
        return classes.Baidu()
    if classes.Barracuda() is not None:
        return classes.Barracuda()
    if classes.Bigip() is not None:
        return classes.Bigip()
    if classes.Binarysec() is not None:
        return classes.Binarysec()
    if classes.Blockdos() is not None:
        return classes.Blockdos()
    if classes.Chinacache() is not None:
        return classes.Chinacache()
    if classes.Ciscoacexml() is not None:
        return classes.Ciscoacexml()
    if classes.Cloudflare() is not None:
        return classes.Cloudflare()
    if classes.Cloudfront() is not None:
        return classes.Cloudfront()
    if classes.Dotdefender() is not None:
        return classes.Dotdefender()
    if classes.Edgecast() is not None:
        return classes.Edgecast()
    if classes.Fortiweb() is not None:
        return classes.Fortiweb()
    if classes.Hyperguard() is not None:
        return classes.Hyperguard()
    if classes.Incapsula() is not None:
        return classes.Incapsula()
    if classes.Isaserver() is not None:
        return classes.Isaserver()
    if classes.Kona() is not None:
        return classes.Kona()
    if classes.Modsecurity() is not None:
        return classes.Modsecurity()
    if classes.Netcontinuum() is not None:
        return classes.Netcontinuum()
    if classes.Paloalto() is not None:
        return classes.Paloalto()
    if classes.Profense() is not None:
        return classes.Profense()
    if classes.Radware() is not None:
        return classes.Radware()
    if classes.Requestvalidationmode() is not None:
        return classes.Requestvalidationmode()
    if classes.Safedog() is not None:
        return classes.Safedog()
    if classes.Secureiis() is not None:
        return classes.Secureiis()
    if classes.Senginx() is not None:
        return classes.Senginx()
    if classes.Sitelock() is not None:
        return classes.Sitelock()
    if classes.Sonicwall() is not None:
        return classes.Sonicwall()
    if classes.Sucuri() is not None:
        return classes.Sucuri()
    if classes.Trafficshield() is not None:
        return classes.Trafficshield()
    if classes.Varnish() is not None:
        return classes.Varnish()
    if classes.Wallarm() is not None:
        return classes.Wallarm()
    if classes.Webknight() is not None:
        return classes.Webknight()
    return "\'\'"


def Scanner():
    for url in urllist:
        content, header = getResponse(url)
        print("targe_url:" + url)
        print("=" * 10 + "Scanner Start" + "=" * 10)

        cms = cmsFinger(content, header)
        # if cms != "":
        print("cms\t\t\t" + ">" * 10 + "\t" + cms)

        frame = frameFinger(content, header)
        # if frame != "":
        print("frame\t\t" + ">" * 10 + "\t" + frame)

        frontend = frontendFinger(content, header)
        # if frontend != "":
        print("frontend\t" + ">" * 10 + "\t" + frontend)

        language = languageFinger(content, header)
        # if language != "":
        print("language\t" + ">" * 10 + "\t" + language)

        server = serverFinger(content, header)
        # if server != "":
        print("server\t\t" + ">" * 10 + "\t" + server)

        system = systemFinger(content, header)
        # if system != "":
        print("system\t\t" + ">" * 10 + "\t" + system)

        waf = wafFinger(content, header)
        # if waf != "":
        print("waf\t\t\t" + ">" * 10 + "\t" + waf)

        print()


if __name__ == '__main__':
    Scanner()
