# -*- coding: utf-8 -*-
import re
import time
import requests
import xlwt  # 进行Excel操作
from random import randint
import threading

# 获取网页内容
def get_onepage_content(url):
    user_agent = [
        'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4482.0 Safari/537.36 Edg/92.0.874.0']
    try:
        response = requests.get(url, headers={'User-Agent': user_agent[randint(0, 1)]})
        if response.status_code == 200:
            # print(response.text)
            return response.text
        return
    except Exception:

        return

# 使用正则表达式提取cve信息字段
def show_cve_content(res):
    match = re.compile(
        '<tr>.*?target="_blank">(.*?)</a></td>.*?<td>(.*?)</td>.*?<button.*?>(.*?)</button>.*?nowrap="nowrap">(.*?)</td>' +
        '.*?<button.*?>(.*?)</button>.*?</tr>', re.S)
    contents = re.findall(match, res)
    for i in range(0,len(contents)):
        content = contents[i]
        content_cp = []
        for j in range(0,len(content)):
            content_cp.append(str(content[j]).strip())
        contents[i] = content_cp
        print(contents[i])
    return contents


# # 保持文件到ali_cve.txt文件中
# def save_content_to_text(content):
#     with open('ali_cve.txt', 'a+', encoding='utf-8') as f:
#         f.write(content + '\n')

def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)  # 创建工作表
    col = ("AVD编号", "漏洞名称", "漏洞类型", "披露时间", "漏洞评分")  # 第一行用于存放列名

    for i in range(0, 5):
        sheet.write(0, i, col[i])  # 列名
    print(len(datalist))
    for i in range(0, len(datalist)):
        # print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 5):
            sheet.write(i + 1, j, data[j])  # 第二行开始，所以用i+1

    book.save(savepath)  # 保存


# 主函数
def main():

    datalist = []
    savepath = ".\\aliyun_vulnerability.xls"  # 当前路径下的文件用.\\

    for pagenum in range(1, 3):
        url = 'https://avd.aliyun.com/nvd/list?page=' + str(pagenum)
        print("你现在爬取的页面url为：%s"%url)

        html = get_onepage_content(url)
        for contents in show_cve_content(html):
            # save_content_to_text(str(contents))
            datalist.append(contents)
        time.sleep(2)
    saveData(datalist,savepath)

    print("数据已爬取完成！！！")



if __name__ == "__main__":
    main()