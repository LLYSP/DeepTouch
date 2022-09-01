import re
class CmsClasses():
    def __init__(self,content,header):
        self.content = content
        self.header = str(header)

    def Drupal(self):
        _ = False
        _ = re.search(r'src="\S*/misc/drupal.js*|Powered by Drupal, an open source content management system',
                      self.content) is not None
        _ |= re.search(r'\S*/misc/drupal.css"|jQuery.extend\WDrupal.settings|Drupal.extend\W', self.content) is not None
        _ |= re.search(r'<meta name="Generator" content="Drupal', self.content) is not None
        if _:
            return "Drupal"
        return None

    def Joomla(self):
        _ = False
        _ = re.search(
            r'/index.php?option=(\S*)|<meta name="generator" content="Joomla*|Powered by <a href="http://www.joomla.org">Joomla!</a>*',
            self.content) is not None
        if _:
            if re.search('/templates/*', self.content, re.I):
                return "Joomla"
        return None

    def Magento(self):
        _ = False
        for x in ('x-magento-init', 'Magento_*', 'images/logo.gif" alt="Magento Commerce" /></a></h1>',
                  '<a href="http://www.magentocommerce.com/bug-tracking" id="bug_tracking_link"><strong>Report All Bugs</strong></a>',
                  '<meta name="keywords" content="Magento, Varien, E-commerce" />', 'mage/cookies.js" ></script>',
                  '<div id="noscript-notice" class="magento-notice">'):
            _ = re.search(x, self.content) is not None
            if _:
                return "Magento"
        return None

    def Wordpress(self):
        _ = False
        for x in ('/wp-admin/', '/wp-content/', '/wp-includes/', '<meta name="generator" content="WordPress'):
            _ = re.search(x, self.content) is not None
        if _:
            return "Wordpress"
        return None
