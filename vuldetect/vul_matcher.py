import xlrd

def detect_vul(service_name, least_rating=8):
    """
    该函数用来识别漏洞库中是否有相应服务版本的漏洞
    输入：service_name即服务名，为str；least_rating为漏洞评分的下限，不超过该值的漏洞不会显示，默认为8
    输出：res，为list，其中每个元素也是一个list，每个list元素包含两个str，第一个是漏洞编号，第二个是漏洞描述
    输出例如：
    [['CVE-2022-31673', 'vmware vrealize_operations 将资源暴露给错误范围'], ['CVE-2022-31656', 'VMware Workspace ONE Access 认证漏洞（CVE-2022-31656）'], ['CVE-2022-31657', 'vmware identity_manager 输出中 
的特殊元素转义处理不恰当（注入）']]
    """
    data = xlrd.open_workbook("./vuldetect/aliyun_vulnerability.xls")
    sheet_name = data.sheet_names()
    table = data.sheet_by_name(sheet_name[0])
    row_num = table.nrows


    res = []
    if '-' in service_name:
        service_name = service_name.split('-', 1)[0]
    for row in range(row_num):
        if service_name.lower() in table.cell_value(row, 1).lower():
            rate = table.cell_value(row, 4)
            if rate != 'N/A':
                if float(rate) >= least_rating:
                    res.append([table.cell_value(row, 0), table.cell_value(row, 1)])

    return res



