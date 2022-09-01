import re


class Blockdos():
    def process(self, headers, content):
        _ = False
        for item in headers.items():
            _ = re.search(r'BlockDos[\.net]*', item[1], re.I) is not None
            if _:
                return "BlockDoS"
