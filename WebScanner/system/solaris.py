import re


class Solaris():
    def process(self, headers, content):
        _ = False
        for item in headers.items():
            _ = re.search(r'solaris|sunos|opensolaris|sparc64|sparc', str(item), re.I) is not None
            if _:
                return "Solaris"
