import re


class Baidu():
    def process(self, headers, content):
        _ = False
        for item in headers.items():
            _ = re.search(r'yunjiasu-nginx', item[1], re.I) is not None
            _ |= re.search(r'YJS-ID', item[1], re.I) is not None
            _ |= re.search(r'fhl', item[1], re.I) is not None
            if _:
                return "Yunjiasu Web Application Firewall (Baidu)"
