import re


class WafClasses():
    def __init__(self, content, header):
        self.content = content
        self.header = str(header)

    def Airlock(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'^AL[_-]SESS[_-]S=\S*', item[1], re.I) is not None
            _ |= re.search(r'X-Airlock-Test', item[0], re.I) is not None
            if _:
                return "InfoGuard Airlock (Phion/Ergon)"
        return None

    def Anquanboa(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'X-Powered-By-Anquanbao', item[0], re.I) is not None
            if _:
                return "Anquanbao Firewall"
        return None

    def Aws(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'aws*', item[1], re.I) is not None
            _ |= re.search(r'x-amz-id-[0-2]', item[0], re.I) is not None
            _ |= re.search(r'x-amz-request-id', item[0], re.I) is not None
            if _:
                return 'Amazon Web Services Web Application Firewall (Amazon)'
        return None

    def Baidu(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'yunjiasu-nginx', item[1], re.I) is not None
            _ |= re.search(r'YJS-ID', item[1], re.I) is not None
            _ |= re.search(r'fhl', item[1], re.I) is not None
            if _:
                return "Yunjiasu Web Application Firewall (Baidu)"
        return None

    def Barracuda(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'barracuda*', item[1], re.I) is not None
            _ |= re.search(r'barra_counter_session=', item[1], re.I) is not None
            _ |= re.search(r'barracuda_', item[1], re.I) is not None
            if _:
                return "Barracuda Web Application Firewall (Barracuda Networks)"
        return None

    def Bigip(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'BigIP|BIGipServer', item[1], re.I) is not None
            _ |= re.search(r'TS\w{4,}=', item[1], re.I) is not None
            _ |= re.search(r'F5', item[1], re.I) is not None

            if _:
                return "BIG-IP Application Security Manager (F5 Networks)"
        return None

    def Binarysec(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'BinarySec', item[1], re.I) is not None
            _ |= re.search(r'x-binarysec-[via|nocahe]', item[0], re.I) is not None

            if _:
                return "BinarySEC Web Application Firewall (BinarySEC)"
        return None

    def Blockdos(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'BlockDos[\.net]*', item[1], re.I) is not None
            if _:
                return "BlockDoS"
        return None

    def Chinacache(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'Powered-By-ChinaCache', item[0], re.I) is not None
            if _:
                return "ChinaCache-CDN"
        return None

    def Ciscoacexml(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'ACE XML Gateway', item[1], re.I) is not None
            if _:
                return "Cisco ACE XML Gateway (Cisco Systems)"
        return None

    def Cloudflare(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'cloudflare[-nginx]', item[1], re.I) is not None
            _ |= re.search(r'__cfduid=', item[1], re.I) is not None
            _ |= re.search(r'cf-ray', item[0], re.I) is not None
            if _:
                return "CloudFlare Web Application Firewall (CloudFlare)"
        return None

    def Cloudfront(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'(cloudfront)', item[1], re.I) is not None
            _ |= re.search('x-amz-cf-id', item[0], re.I) is not None
            if _:
                return "CloudFront Web Application Firewall (Amazon)"
        return None

    def Dotdefender(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'X-dotDefender-denied', item[0], re.I) is not None
            if _:
                return "dotDefender Web Application Firewall (Applicure Technologies)"
        return None

    def Edgecast(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'ECDF', item[1], re.I) is not None
            if _:
                return "EdgeCast Web Application Firewall (Verizon)"
        return None

    def Fortiweb(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'FORTIWAFSID=', item[1], re.I) is not None
            if _:
                return "FortiWeb Web Application Firewall (Fortinet)"
        return None

    def Hyperguard(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'^WODSESSION=', item[1], re.I) is not None
            if _:
                return "Hyperguard Web Application Firewall (art of defence)"
        return None

    def Incapsula(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'incap_ses|visid_incap|Incapsula', item[1], re.I) is not None
            if _:
                return "Incapsula Web Application Firewall (Incapsula/Imperva)"
        return None

    def Isaserver(self):
        try:
            _ = False
            _ = re.search(
                r'The server denied the specified Uniform Resource Locator (URL). Contact the server administrator.',
                self.content, re.I) is not None
            _ |= re.search(r'The ISA Server denied the specified Uniform Resource Locator (URL)', self.content,
                           re.I) is not None
            if _:
                return "ISA Server (Microsoft)"
        except Exception as e:
            print("IsaServer Problem ", e)
        return None

    def Kona(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'AkamaiGHost|Kona', item[1], re.I) is not None
            if _:
                return "Kona Web Application Firewall (Akamai)"
        return None

    def Modsecurity(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'Mod_Security|NOYB', item[1], re.I) is not None
            if _:
                return "ModSecurity Web Application Firewall (Trustwave)"
        return None

    def Netcontinuum(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'NCI__SessionId=', item[1], re.I) is not None
            if _:
                return "NetContinuum Web Application Firewall (NetContinuum/Barracuda Networks)"
        return None

    def Paloalto(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'MISS from PaloAlto', item[1], re.I) is not None
            if _:
                return "Palo Alto Firewall (Palo Alto Networks)"
        return None

    def Profense(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'PLBSID=', item[1], re.I) is not None
            _ = re.search(r'Profense', item[1], re.I) is not None
            if _:
                return "Profense Web Application Firewall (Armorlogic)"
        return None

    def Radware(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'X-SL-CompState', item[0], re.I) is not None
            if _:
                return "AppWall Web Application Firewall (Radware)"
        return None

    def Requestvalidationmode(self):
        _ = False
        _ = re.search(r'ASP.NET has detected data in the request that is potentially dangerous', self.content,
                      re.I) is not None
        _ |= re.search(r'Request Validation has detected a potentially dangerous client input value', self.content,
                       re.I) is not None
        if _:
            return "ASP.NET RequestValidationMode (Microsoft)"
        return None

    def Safedog(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'WAF/2\.0', item[1], re.I) is not None
            _ |= re.search(r'Safedog', item[1], re.I) is not None
            if _:
                return "Safedog Web Application Firewall (Safedog)"
        return None

    def Secureiis(self):
        _ = False
        _ = re.search(r'SecureIIS[^<]+Web Server Protection', self.content, re.I) is not None
        _ |= re.search(r'http://www.eeye.com/SecureIIS/', self.content, re.I) is not None
        _ |= re.search(r'\?subject=[^>]*SecureIIS Error', self.content, re.I) is not None
        if _:
            return "SecureIIS Web Server Security (BeyondTrust)"
        return None

    def Senginx(self):
        _ = False
        _ = re.search(r'SENGINX-ROBOT-MITIGATION', self.content, re.I) is not None
        if _:
            return "SEnginx (Neusoft Corporation)"
        return None

    def Sitelock(self):
        _ = False
        _ = re.search(r'SiteLock Incident ID', self.content, re.I) is not None
        if _:
            return "TrueShield Web Application Firewall (SiteLock)"
        return None

    def Sonicwall(self):
        _ = False
        _ = re.search(r'This request is blocked by the SonicWALL', self.content, re.I) is not None
        _ |= re.search(r'Web Site Blocked.+\bnsa_banner', self.content, re.I) is not None
        if _:
            return "SonicWALL (Dell)"
        return None

    def Sucuri(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'Sucuri|Cloudproxy', item[1], re.I) is not None
            _ |= re.search(r'X-Sucuri-ID', item[0], re.I) is not None
            if _:
                return "CloudProxy WebSite Firewall (Sucuri)"
        return None

    def Trafficshield(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'F5-TrafficShield', item[1], re.I) is not None
            _ |= re.search(r'ASINFO=', item[1], re.I) is not None
            if _:
                return "TrafficShield (F5 Networks)"
        return None

    def Varnish(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'X-Varnish', item[0], re.I) is not None
            _ |= re.search(r'varnish*', item[1], re.I) is not None
            if _:
                return "Varnish FireWall (OWASP)"
        return None

    def Wallarm(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'nginx-wallarm', item[1], re.I) is not None
            if _:
                return "Wallarm Web Application Firewall (Wallarm)"
        return None

    def Webknight(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'Webknight', item[1], re.I) is not None
            if _:
                return "WebKnight Application Firewall (AQTRONIX)"
        return None
