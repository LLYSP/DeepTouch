import re

class Mootools():
    def process(self, headers, content):
        _ = False
        _ = re.search(r'MooTools-[0-9\-\.]+.js', content, re.I) is not None
        if _:
            return "MooTools"
