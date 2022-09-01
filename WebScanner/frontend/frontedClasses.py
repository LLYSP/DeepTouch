import re
class FrontendClasses():
    def __init__(self,content,header):
        self.content = content
        self.header = str(header)

    def Angularjs(self):
        _ = False
        _ = re.search(r'ng-app', self.content, re.I) is not None
        _ |= re.search(r'ng-version', self.content, re.I) is not None
        _ |= re.search(r'app-root', self.content, re.I) is not None
        if _:
            return "AngularJS"
        return None

    def Emberjs(self):
        _ = False
        _ = re.search(r'ember-view', self.header, re.I) is not None
        if _:
            return "EmberJs"
        return None

    def Jquery(self):
        res = re.findall(r'jquery-([0-9\-.]+).js|jquery', self.content, re.I)
        res2 = re.findall(r'jquery/([0-9\-.]+)/', self.content, re.I)
        res3 = re.findall(r'jquery-([0-9\-.]+).min.js', self.content, re.I)
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
        return None

    def Knockout(self):
        _ = False
        _ = re.search(r'knockout-[0-9\-\.]+.js', self.content, re.I) is not None
        if _:
            return "Knockout"
        return None

    def Meteorjs(self):
        _ = False
        _ = re.search(r'__meteor_runtime_config__', self.content, re.I) is not None
        if _:
            return "MeteorJS"
        return None

    def Mootools(self):
        _ = False
        _ = re.search(r'MooTools-[0-9\-\.]+.js', self.content, re.I) is not None
        if _:
            return "MooTools"
        return None

    def Prototype(self):
        _ = False
        _ = re.search(r'prototype.js', self.content, re.I) is not None
        _ |= re.search(r'prototype-[0-9\-\.]+.js', self.content, re.I) is not None
        if _:
            return "Prototype"
        return None

    def Reactjs(self):
        _ = False
        _ = re.search(r'react-[0-9\-\.]+.js', self.content, re.I) is not None
        _ = re.search(r'reactroot|reactid', self.content, re.I) is not None
        if _:
            return "ReactJS"
        return None

    def Vuejs(self):
        _ = False
        _ |= re.search(r'v-bind|v-for|v-if', self.content, re.I) is not None
        if _:
            return "VueJS"
        return None