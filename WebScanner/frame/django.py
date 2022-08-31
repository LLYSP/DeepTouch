import re


class Django():
    def process(self, headers, content):
        _ = False
        for item in headers.items():
            _ = re.search(r'csrftoken=', item[1], re.I) is not None
            if _:
                return "Django (Python)"
