import socket
import re


def Extra_Scan(host, port, probe):
    """
    该函数使用其他的探针进行嗅探
    输入：ip，单个port，list格式的相应probe数据
    输出：如果没有匹配就为0，如果有匹配输出一条string，内容为端口号与服务与版本（如果识别到版本）
    """
    
    # 判断发送tcp还是udp包
    global client_socket
    if probe["protocol"] == "TCP":
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    elif probe["protocol"] == "UDP":
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    feedback = None
    if probe["totalwaitms"] is not None:
        client_socket.settimeout(1)  # 为增加速度，使用1，正式应该为int(probe["totalwaitms"])//1000
    else:
        client_socket.settimeout(5)
    payload = eval(repr(probe["probestring"]).replace('\\\\', '\\'))
    
    # 尝试建立连接并发送payload
    try:
        client_socket.connect((host, port))
        client_socket.sendall(payload.encode("utf-8"))
    except Exception as e:
        return 0
    
    # 尝试接收报文
    try:
        feedback = client_socket.recv(1024).decode("raw_unicode_escape")  # 不知道为啥要用raw_unicode_escape
    except Exception as e:
        return 0
    finally:
        # 匹配部分
        if feedback is not None:
            for each in probe["matches"]:
                pattern_str = each["pattern"]  # 提取原始的pattern字符串
                p_pattern = re.compile(pattern_str)
                res_pattern = p_pattern.search(feedback)  # 正则匹配原始的pattern
                if res_pattern is not None:  # 如果匹配成功
                    res = {"service": "", "version": ""}  # 生成res
                    res["service"] = each["name"]  # 如果匹配成功必然有服务名
                    version = each["versioninfo"]["version"]  # 尝试获取版本号，在数据库中不一定有
                    if version is not None:  # 如果有相应version信息
                        p = re.compile(r'\$\d')
                        # 由于数据库中的version键值对会根据pattern匹配的结果进行填充，这里需要在version中提取类似$1的字符并进行替换
                        res_p = re.findall(p, version)  # 使用正则匹配字符$1等
                        for i in range(len(res_p)):  # 找到后根据相应的顺序进行替换
                            version = version.replace(res_p[i], res_pattern.group(int(res_p[i][1])))
                        string = "[+]On port " + str(port) + "\nService: " + res["service"] + " | Version: " + version
                        return [port, res['service'], version, string]
                    else:
                        string = "[+]On port " + str(port) + "\nService: " + res["service"]
                        return [port, res['service'], string]
    
    client_socket.close()
    return 0

