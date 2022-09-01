import json
from ServiceScanner.NULL_Scan import NULL_Scan
from ServiceScanner.Extra_Scan import Extra_Scan


def Service_Scan(host, port):
    """
    Service_Scan函数，进行端口上相应服务与版本的识别
    输入：host，一个str；portlist，以list形式呈现的所有port，其中所有port都是int
    输出：report，其本身是一个list，存储string，作为list包含所有的结果，如果为空表示服务识别失败
    """

    report = []
    # Step1: TCP NULL探针
    # 打开json文件，调取相应探针信息并进行搜索
    with open('ServiceScanner/service_dictionary.json', encoding='utf-8') as service_fingerprint:
        Null_probe = json.load(service_fingerprint)[0]  # load是json库用来加载文件的函数
    result = NULL_Scan(host, port, Null_probe)  # 对于需要的端口调用TCP_NULL_Scan进行扫描。
    if result != 0:
        return result

    # Step2: 所有其他探针
    # 打开json文件，调取所有探针信息并进行搜索
    with open('ServiceScanner/service_dictionary.json', encoding='utf-8') as service_fingerprint:
        All_probe = json.load(service_fingerprint)
        for i in range(len(All_probe)):  # 检查所要嗅探的端口是否在已有的portlist中
            ports = All_probe[i]["ports"]
            if str(port) in ports:
                result = Extra_Scan(host, port, All_probe[i])
                if result != 0:
                    return result

    return report


