import platform
import sys
import threading
import time
from optparse import OptionParser

import scan_port
import scan_OS

if __name__ == '__main__':
    start_time = time.time()
    if len(sys.argv) < 2:
        print("请输入要扫描的主机地址，如：192.168.1.1")
        sys.exit()
    host = sys.argv[2]  # 在终端输入ip

    # 以下注释部分属于获取操作系统版本的nmap，还没调试完成
    # parser = OptionParser("Usage:%prog -i <target host> -n <network> or -t ttl_scan")  # 输出帮助信息
    # parser.add_option('-i', type='string', dest='tgtIP', help='specify target host')  # 获取ip地址参数
    # parser.add_option('-t', type='string', dest='ttl', help='input -t ttl')  # 是否使用ttl模块扫描
    # parser.add_option('-n', type="string", dest='tgtNetwork', help='specify target host')  # 获取网段信息
    # options, args = parser.parse_args()
    # # 实例化用户的参数
    # tgtip = options.tgtIP
    # Network = options.tgtNetwork
    # TTL = options.ttl
    #
    # if tgtip is None and Network is None:  # 判断文件是否存在
    #     print(parser.usage)
    #     sys.exit()
    #
    # if tgtip is not None:  # 单个地址时执行的操作
    #     if TTL:  # 判断是否调用ttl扫描
    #         scan_OS.ttl_scan(tgtip)
    #     else:
    #         scan_OS.nmap_scan(tgtip)
    #
    # if Network:
    #     prefix = Network.split(".")[0] + '.' + Network.split(".")[1] + '.' + Network.split(".")[2] + '.'  # 以点为分割提取ip
    #     # 地址前三位
    #
    #     if TTL:  # 判断是否调用ttl扫描
    #         for i in range(1, 255):
    #             ip = prefix + str(i)  # 结合ip地址前缀生成网段扫描所需ip
    #             t = threading.Thread(target=scan_OS.ttl_scan, args=(ip,))
    #             t.start()
    #             time.sleep(0.1)
    #     else:
    #         for i in range(1, 255):
    #             ip = prefix + str(i)
    #             t = threading.Thread(target=scan_OS.nmap_scan, args=(ip,))
    #             t.start()




    thread_list = []

    # 线程池
    # with ThreadPoolExecutor(1000) as t:
    #     for port in range(1,2000):
    #         t.submit(scan_port(host,port))
    # 多线程
    for port in range(1, 2000):
        t = threading.Thread(target=scan_port.scan_port, args=(host, port))
        thread_list.append(t)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:  # 能按顺序输出
        thread.join()

    end_time = time.time()
    print(f"耗时{end_time - start_time}")
