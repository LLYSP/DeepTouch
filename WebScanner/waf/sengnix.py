import re


class Senginx():
    def process(self, headers, content):
        _ = False
        _ = re.search(r'SENGINX-ROBOT-MITIGATION', content, re.I) is not None
        if _:
            return "SEnginx (Neusoft Corporation)"
