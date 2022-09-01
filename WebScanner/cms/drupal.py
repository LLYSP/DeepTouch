import re

class Drupal():

    def process(self, headers, content):
        _ = False

        _ = re.search(r'src="\S*/misc/drupal.js*|Powered by Drupal, an open source content management system',
                      content) is not None
        _ |= re.search(r'\S*/misc/drupal.css"|jQuery.extend\WDrupal.settings|Drupal.extend\W', content) is not None
        _ |= re.search(r'<meta name="Generator" content="Drupal', content) is not None
        if _:
            return "Drupal"

