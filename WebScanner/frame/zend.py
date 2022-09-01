import re

class Zend():
    def process(self, headers, content):
        _ = False
        for item in headers.items():
            _ = re.search(r'Zend', item[1], re.I) is not None
            if _:
                return "Zend (PHP)"
