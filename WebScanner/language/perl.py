import re


class Perl():
    def process(self, headers, content):
        _ = False
        _ = re.search(r'\.pl$|\.cgi$', content) is not None
        if _:
            return "Perl"
