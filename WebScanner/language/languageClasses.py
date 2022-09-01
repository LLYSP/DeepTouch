import re
class LanguageClasses():
    def __init__(self,content,header):
        self.content = content
        self.header = str(header)

    def Asp(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'ASP.NET|X-AspNet-Version|x-aspnetmvc-version', str(item), re.I) is not None
            if not _:
                _ |= re.search(r'(__VIEWSTATE\W*)', self.content) is not None
            if not _:
                _ |= re.search(r'\.asp$|\.aspx$', self.content) is not None
            if _:
                return "ASP.NET"
        return None

    def Java(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'Java|Servlet|JSP|JBoss|Glassfish|Oracle|JRE|JDK|JSESSIONID', str(item)) is not None
            if not _:
                _ |= re.search(r'\.jsp$|\.jspx$|.do$|\.wss$|\.action$', self.content) is not None
            if _:
                return "Java"
        return None

    def Perl(self):
        _ = False
        _ = re.search(r'\.pl$|\.cgi$', self.content) is not None
        if _:
            return "Perl"
        return None

    def Php(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'X-PHP-PID|PHP\S*|PHPSESSID', str(item)) is not None
        _ |= re.search(r'\.php$|\.phtml$', self.content) is not None
        if _:
            return "PHP"
        return None

    def Python(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'python|zope|zserver|wsgi|plone|_ZopeId', item[1], re.I) is not None
        _ |= re.search(r'\.py$', self.content) is not None
        if _:
            return "Python"
        return None

    def Ruby(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r"mod_rack|phusion|passenger", item[1], re.I) is not None
        _ |= re.search(r'\.rb$|\.rhtml$', self.content) is not None
        if _:
            return "Ruby"
        return None
