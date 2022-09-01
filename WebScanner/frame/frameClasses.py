import re
class FrameClasses():
    def __init__(self,content,header):
        self.content = content
        self.header = str(header)

    def Cakephp(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'cakephp=', item[1], re.I) is not None
            if _:
                return "CakePHP (PHP)"
        return None

    def Cherrypy(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'CherryPy', item[1], re.I) is not None
            if _:
                return "CherryPy (Python)"
        return None

    def Dancer(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ |= re.search(r'Dancer|dancer\.session=.*', item[1], re.I) is not None
        if _:
            return "Dancer (Perl)"
        return None

    def Django(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'csrftoken=', item[1], re.I) is not None
            if _:
                return "Django (Python)"
        return None

    def Flask(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'flask', item[1], re.IGNORECASE) is not None
            if _:
                return "Flask (Python)"
        return None

    def Fuelphp(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'fuelcid=', item[1], re.I) is not None
            _ |= re.search(r'Powered by <a href="http://fuelphp.com">FuelPHP</a>', self.content) is not None
            if _:
                return "FuelPHP (PHP)"
        return None

    def Grails(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'Grails', item[1], re.I) is not None
            _ |= re.search(r'X-Grails|X-Grails-Cached', item[0], re.I) is not None
            if _:
                return "Grails (Java)"
        return None

    def Laravel(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'laravel_session=', item[1], re.I) is not None
            if _:
                return "Laravel (PHP)"
        return None

    def Mvc(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'x-aspnetmvc-version|__requestverificationtoken', str(item), re.I) is not None
            if _:
                return "ASP.NET MVC"
        return None

    def Nette(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'nette*|nette-browser=*', item[1], re.I) is not None
            if _:
                return "Nette (PHP)"
        return None

    def Phalcon(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'phalcon-auth-*', item[1], re.I) is not None
            _ |= re.search(r'Phalcon [(https://phalconphp.com/)]*', item[1]) is not None
            if _:
                return "Phalcon (C and PHP)"
        return None

    def Rails(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'rails*|_rails_admin_session=*|x-rails', item[1], re.I) is not None
            _ |= re.search(r'rails*|x-rails', item[0], re.I) is not None
            if _:
                return "Rails (Ruby)"
        return None

    def Symfony(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'symfony=*', item[1], re.I) is not None
            if _:
                return "Symfony PHP"
        return None

    def Yii(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'_csrf=*', item[1], re.I) is not None
            _ |= re.search(r'Powered by <a href="http://www.yiiframework.com/" rel="external">Yii Framework</a>',
                           self.content) is not None
            if _:
                return "Yiiframework (PHP)"
        return None

    def Zend(self):
        header_dictionary = eval(self.header)
        _ = False
        for item in header_dictionary.items():
            _ = re.search(r'Zend', item[1], re.I) is not None
            if _:
                return "Zend (PHP)"
        return None

