import re


class Yii():
    def process(self, headers, content):
        _ = False
        for item in headers.items():
            _ = re.search(r'_csrf=*', item[1], re.I) is not None
            _ |= re.search(r'Powered by <a href="http://www.yiiframework.com/" rel="external">Yii Framework</a>',
                           content) is not None
            if _:
                return "Yiiframework (PHP)"
