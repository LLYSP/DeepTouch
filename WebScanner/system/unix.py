import re


class Unix():
    def process(self, headers, content):
        _ = False
        for item in headers.items():
            _ = re.search(r'unix', str(item), re.I) is not None
            if _:
                return "Unix"
