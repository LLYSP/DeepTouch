import os
import platform
import re

class IP2MAC:
    """
    Python3根据IP地址获取MAC地址（不能获取本机IP，可以获取与本机同局域网设备IP的MAC）
    """
    def __init__(self):
        self.patt_mac = re.compile('([a-f0-9]{2}[-:]){5}[a-f0-9]{2}', re.I)

    def getMac(self, ip):
        sysstr = platform.system()

        if sysstr == 'Windows':
            macaddr = self.__forWin(ip)
        elif sysstr == 'Linux':
            macaddr = self.__forLinux(ip)
        else:
            macaddr = None

        return macaddr or '00-00-00-00-00-00'

    def __forWin(self, ip):
        os.popen('ping -n 1 -w 500 {} > nul'.format(ip))
        macaddr = os.popen('arp -a {}'.format(ip))
        macaddr = self.patt_mac.search(macaddr.read())

        if macaddr:
            macaddr = macaddr.group()
        else:
            macaddr = None

        return macaddr

    def __forLinux(self, ip):
        os.popen('ping -nq -c 1 -W 500 {} > /dev/null'.format(ip))

        result = os.popen('arp -an {}'.format(ip))

        result = self.patt_mac.search(result.read())

        return result.group() if result else None

class MAC2Device:
    def sliceMac(self,mac):
        mac_measurable = mac.replace('-','')[0:6]
        # print(mac_measurable)
        return mac_measurable

    def match_device(self,mac_measurable,res):
        file = open(res,encoding='UTF-8')
        for line in file.readlines():
            curLine = line.strip()
            Registry,Assignment,Organization_info = curLine.split(',',2)
            if Assignment == mac_measurable.upper():
                return Organization_info
        return "Not Found"

if __name__ == '__main__':
    iplist = [
        "10.122.192.1",
        "10.122.203.46",
        "10.122.203.193"
    ]
    msg_list = []
    for ip in iplist:
        g = IP2MAC()
        mac = g.getMac(ip)

        if mac != '00-00-00-00-00-00':
            mac_tool = MAC2Device()
            mac_measurable = mac_tool.sliceMac(mac)
            res = "./device.txt"
            info = mac_tool.match_device(mac_measurable,res)
            msg_list.append([ip,mac,info])
    print(msg_list)


