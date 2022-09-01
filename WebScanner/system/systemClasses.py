import re
class SystemClasses():
    def __init__(self,content,header):
        self.content = content
        self.header = str(header)

    def Bsd(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'\S*BSD', str(item), re.I) is not None
            if _:
                return "BSD"
        return None

    def Linux(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.findall(
                r'linux|ubuntu|gentoo|debian|dotdeb|centos|redhat|sarge|etch|lenny|squeeze|wheezy|jessie|red hat|scientific linux',
                str(item), re.I)
            if _:
                if len(_) == 2:
                    return _[0]
                else:
                    return _[0]
        return None

    def Mac(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'Mac|MacOS|MacOS\S*', str(item)) is not None
            if _:
                return "MacOS"
        return None

    def Solaris(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'solaris|sunos|opensolaris|sparc64|sparc', str(item), re.I) is not None
            if _:
                return "Solaris"
        return None

    def Unix(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'unix', str(item), re.I) is not None
            if _:
                return "Unix"
        return None

    def Windows(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'windows|win32', str(item), re.I) is not None
            if _:
                return "Windows"
        return None