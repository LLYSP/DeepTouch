# -*- coding utf-8 -*-
import socket
import sys
import threading
import time
import platform
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def ip_validation(host):
    try:
        socket.inet_aton(host)
        # 把16位正整数从主机字节序转换成网络序ipv4,查看格式是否正确
        return True
    except socket.error:
        return False


def scan_port(host, port):
    if not ip_validation(host):
        return False
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 服务器之间的通信,走TCP协议
        sock.settimeout(2)
        # 判断超时时间为2秒
        result = sock.connect_ex((host, port))
        # 判断端口是否开放，连接成功返回0
        if result == 0:
            print("{+}" + host + ":" + str(port) + ">" * 20 + find_service_name(port))

        # else:
        #     print("{-}"+host+":"+str(port)+">"*20,"close")
        sock.close()
    except:
        pass


def find_service_name(port):  # 根据端口判断服务
    return socket.getservbyport(port)
