import sys
import socket


def scan_port(ip, port):
    OPEN_MSG = "% 6d [OPEN]\n"
    timeout = 5
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        result_code = s.connect_ex((ip, port))  # 开放放回0
        if result_code == 0:
            # print(OPEN_MSG % port) # print不适合多线程
            sys.stdout.write(ip + "     " + OPEN_MSG % port)

            print("{+}" + ip + ":" + str(port) + ">" * 20 + find_service_name(port))
        # else:
        #     sys.stdout.write("% 6d [CLOSED]\n" % port)
    except:
        pass
    finally:
        s.close()


def find_service_name(port):  # 根据端口判断服务
    return socket.getservbyport(port)
