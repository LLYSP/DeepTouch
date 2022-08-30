# -*- coding: utf-8 -*-
import re
import time
import requests
from random import randint
import threading
import pymysql
import MySQLdb

# thread_lock = threading.BoundedSemaphore(value=10)

# dbhost = "localhost"
# dbuser = "root"
# dbpass = "123456"
# dbname = "ali_cve"
print('正在连接到mysql服务器...')
# 给定要连接的数据库IP地址、用户名、密码、数据库名
db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="ali_cve")
#db = MySQLdb.connect(
 # host="127.0.0.1",
 # user="root",
  #passwd="123456",
  #charset="utf8",
   # db = "ali_cve"
#)
print('连接成功!')
# 创建一个游标对象 cursor
cursor = db.cursor()
# 执行SQL语句
cursor.execute("SHOW TABLES")
# 获取所有记录列表
result = cursor.fetchall()
print("当前的表为：%s" % result)


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
    # print(contents)
    # for content in contents:
    # yield {
    #     'cve_id'   : content[0].strip(),
    #     'vul_name' : content[1],
    #     'vul_type' : content[2].strip(),
    #     'cve_date' : content[-2].strip(),
    #     'cvss_level': content[-1].strip()
    # }
    # content = list(content)
    return contents


# 保持文件到ali_cve.txt文件中
def save_content_to_text(content):
    with open('ali_cve.txt', 'a+', encoding='utf-8') as f:
        f.write(content + '\n')


# 数据插入mysql数据库
def save_to_mysql(content):
    global cve_id, vul_name, vul_type, cve_date, cvss_level
    cve_id = content[0]
    vul_name = content[1]
    vul_type = content[2]
    cve_date = content[3]
    cvss_level = content[4]
    values = (cve_id, vul_name, vul_type, cve_date, cvss_level)
    # 插入数据语句
    query = """INSERT INTO cve_detail (cve_id, vul_name, vul_type, cve_date, cvss_level) values (%s, %s, %s, %s, %s)"""
    try:
        cursor.execute(query, values)
        print("数据插入Successful")
        db.commit()
    except:
        pass
    # # 写入完成后解锁
    # thread_lock.release()


# 主函数
def main():
    for pagenum in range(1, 5474):
        url = 'https://avd.aliyun.com/nvd/list?page=' + str(pagenum)
        html = get_onepage_content(url)
        # print(html)
        for content in show_cve_content(html):
            # print(content)
            content = list(content)
            for i in range(0, len(content)):
                content[i] = content[i].strip()  # 去除字符串中的空格

            # 上锁
            # thread_lock.acquire()
            # task = threading.Thread(target=save_to_mysql, args=(content))
            # task.start()
            # 写入数据库
            save_to_mysql(content)

    # 关闭游标，提交，关闭数据库连接
    # 如果没有这些关闭操作，执行后在数据库中查看不到数据
    cursor.close()
    db.commit()
    db.close()
    # for pagenum in range(1, 500):
    #     url = 'https://avd.aliyun.com/nvd/list?page=' + str(pagenum)
    #     print("你现在爬取的页面url为：%s"%url)
    #
    #     html = get_onepage_content(url)
    #     for content in show_cve_content(html):
    #         save_content_to_text(str(content))
    #     time.sleep(2)
    #
    print("数据已爬取完成！！！")


if __name__ == "__main__":
    main()
