import re


class Mac():
    def process(self, headers, content):
        _ = False
        for item in headers.items():
            _ = re.search(r'Mac|MacOS|MacOS\S*', str(item)) is not None
            if _:
                return "MacOS"
