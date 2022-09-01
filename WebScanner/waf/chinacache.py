import re


class Chinacache():
    def process(self, headers, content):
        _ = False
        for item in headers.items():
            _ = re.search(r'Powered-By-ChinaCache', item[0], re.I) is not None
            if _:
                return "ChinaCache-CDN"
