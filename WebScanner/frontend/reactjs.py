import re

class Reactjs():
    def process(self, headers, content):
        _ = False
        _ = re.search(r'react-[0-9\-\.]+.js', content, re.I) is not None
        _ = re.search(r'reactroot|reactid', content, re.I) is not None
        if _:
            return "ReactJS"
