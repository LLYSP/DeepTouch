import re


class Ciscoacexml():
    def process(self, headers, content):
        _ = False
        for item in headers.items():
            _ = re.search(r'ACE XML Gateway', item[1], re.I) is not None
            if _:
                return "Cisco ACE XML Gateway (Cisco Systems)"
