import re

class Wordpress():

    def process(self, headers, content):
        _ = False

        for x in ('/wp-admin/', '/wp-content/', '/wp-includes/', '<meta name="generator" content="WordPress'):
            _ = re.search(x, content) is not None
        if _:
            return "Wordpress"

