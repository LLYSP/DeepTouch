import re

class Knockout():
    def process(self, headers, content):
        _ = False
        _ = re.search(r'knockout-[0-9\-\.]+.js', content, re.I) is not None
        if _:
            return "Knockout"
