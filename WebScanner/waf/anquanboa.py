import re


class Anquanboa():
    def process(self, headers, content):
        _ = False
        for item in headers.items():
            _ = re.search(r'X-Powered-By-Anquanbao', item[0], re.I) is not None
            if _:
                return "Anquanbao Firewall"
