import re

class Prototype():
    def process(self, headers, content):
        _ = False
        _ = re.search(r'prototype.js', content, re.I) is not None
        _ |= re.search(r'prototype-[0-9\-\.]+.js', content, re.I) is not None
        if _:
            return "Prototype"
