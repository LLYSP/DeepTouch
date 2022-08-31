import re

class Vuejs():
    def process(self, headers, content):
        _ = False
        _ |= re.search(r'v-bind|v-for|v-if', content, re.I) is not None
        if _:
            return "VueJS"
