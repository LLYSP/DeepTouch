import re


class Cherrypy():
    def process(self, headers, content):
        _ = False
        for item in headers.items():
            _ = re.search(r'CherryPy', item[1], re.I) is not None
            if _:
                return "CherryPy (Python)"
