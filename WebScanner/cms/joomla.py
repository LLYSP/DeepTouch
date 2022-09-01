import re

class Joomla():

    def process(self, headers, content):
        _ = False

        _ = re.search(
            r'/index.php?option=(\S*)|<meta name="generator" content="Joomla*|Powered by <a href="http://www.joomla.org">Joomla!</a>*',
            content) is not None
        if _:
            if re.search('/templates/*', content, re.I):
                return "Joomla"

