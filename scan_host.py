import logging

from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1


def ttl_scan(ip,ip_list):  # 探测ip
    try:
        packet = IP(dst=ip) / ICMP()
        result = sr1(packet, timeout=1, verbose=0)
        if result is None:
            logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
            pass

        elif int(result[IP].ttl) <= 64:  # 判断目标主机响应包中TTL值是否小于等于64
            print("%s  is Linux/Unix" % ip)  # 是的话就为linux/Unix
            ip_list.append(ip)

        else:
            print("%s is Windows" % ip)  # 反之就是windows
            ip_list.append(ip)
    except:
        pass