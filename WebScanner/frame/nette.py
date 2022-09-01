import re


class Nette():
    def process(self, headers, content):
        _ = False
        for item in headers.items():
            _ = re.search(r'nette*|nette-browser=*', item[1], re.I) is not None
            if _:
                return "Nette (PHP)"
