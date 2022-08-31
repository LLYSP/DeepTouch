import re

class Meteorjs():
    def process(self, headers, content):
        _ = False
        _ = re.search(r'__meteor_runtime_config__', content, re.I) is not None
        if _:
            return "MeteorJS"
