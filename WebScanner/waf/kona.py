import re


class Kona():
    def process(self, headers, content):
        _ = False
        for item in headers.items():
            _ = re.search(r'AkamaiGHost|Kona', item[1], re.I) is not None
            if _:
                return "Kona Web Application Firewall (Akamai)"
