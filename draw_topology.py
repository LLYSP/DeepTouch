import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import re
import subprocess
import socket


def getIp2TXT(url,res):
    subprocess.call("tracert " + url + " > "+res, shell=True)


def generateIpList(res):
    file = open(res)
    iplist = []
    for line in file.readlines():
        curLine = line.strip()
        pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+)')  # 正则表达式，匹配IP地址
        ip = pattern.findall(curLine)  # 获取ip地址
        if len(ip) > 0:
            iplist.append(ip[0])
    return iplist


def drawPic(host_ip, iplist_list):
    my_dpi = 96
    plt.figure(figsize=(480 / my_dpi, 480 / my_dpi), dpi=my_dpi)
    fromlist = []
    tolist = []

    for iplist in iplist_list:
        fromlist.append(host_ip)
        for ip in iplist:
            target = iplist[0]
            if ip != target:
                fromlist.append(ip)
                tolist.append(ip)
        tolist.append(target)

    df = pd.DataFrame({'from': fromlist, 'to': tolist})
    print(fromlist)
    print(tolist)
    G = nx.from_pandas_edgelist(df, 'from', 'to')

    nx.draw(G, with_labels=True, node_size=50, node_color="skyblue", node_shape="o", alpha=0.5, linewidths=4,
            font_size=5, font_color="grey", font_weight="bold", width=1, edge_color="grey")

    plt.show()


def get_host_ip():
    """
    查询本机ip地址
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip
