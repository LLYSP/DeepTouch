import re


class Windows():
    def process(self, headers, content):
        _ = False
        for item in headers.items():
            _ = re.search(r'windows|win32', str(item), re.I) is not None
            if _:
                return "Windows"
