import re


class Paloalto():
    def process(self, headers, content):
        _ = False
        for item in headers.items():
            _ = re.search(r'MISS from PaloAlto', item[1], re.I) is not None
            if _:
                return "Palo Alto Firewall (Palo Alto Networks)"
