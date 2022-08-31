import re

class Jquery():
    def process(self, headers, content):
        print(content)
        res = re.findall(r'jquery-([0-9\-.]+).js|jquery', content, re.I)
        res2 = re.findall(r'jquery/([0-9\-.]+)/', content, re.I)
        res3 = re.findall(r'jquery-([0-9\-.]+).min.js', content, re.I)
        if res is not None:
            for item in res:
                if item != "":
                    return "jquery" + item
            for item in res2:
                if item != "":
                    return "jquery" + item
            for item in res3:
                if item != "":
                    return "jquery" + item
            return "jquery"
