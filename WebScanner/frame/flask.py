import re


class Flask():
    def process(self, headers, content):
        _ = False
        for item in headers.items():
            _ = re.search(r'flask', item[1], re.IGNORECASE) is not None
            if _:
                return "Flask (Python)"
