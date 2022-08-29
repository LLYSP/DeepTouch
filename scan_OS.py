from telnetlib import IP

import nmap
import sys
import time
from optparse import OptionParser
from threading import Thread
from scapy.all import *
from scapy.layers.inet import ICMP


def ttl_scan(ip):#简易扫描
    packet = IP(dst=ip) / ICMP()
    result = sr1(packet, timeout=1, verbose=0)
    if result is None:
        pass

    elif int(result[IP].ttl) <= 64:  # 判断目标主机响应包中TTL值是否小于等于64
        print("%s  is Linux/Unix" % ip)  # 是的话就为linux/Unix

    else:
        print("%s is Windwows" % ip)  # 反之就是linux


def nmap_scan(ip):#复杂扫描nmap
    nm = nmap.PortScanner()
    try:
        result = nm.scan(hosts=ip, arguments='-0')  # 调用nmap执行-O扫描操作系统
        os = result['scan'][ip]['osmatch'][0]['name']
        time.sleep(0.1)
        print(ip, os)
    except:
        pass
