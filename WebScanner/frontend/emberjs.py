import re

class Emberjs():
    def process(self, headers, content):
        _ = False
        for item in headers.items():
            _ = re.search(r'ember-view', item[1], re.I) is not None
            if _:
                return "EmberJs"
