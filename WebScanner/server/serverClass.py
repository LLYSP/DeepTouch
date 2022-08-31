import re
class ServerClass():
    def __init__(self,content,header):
        self.content = content
        self.header = str(header)

    def findServer(self):
        server="NULL"
        header_dictionary = eval(self.header)
        for item in header_dictionary.items():
            if re.search(r'server', item[0], re.I):
                server = item[1]
        return server
