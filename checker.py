import requests
import urllib3
from colorama import Fore
from colorama import init


# Source Code: https://github.com/pythonism/proxy-checker

class checker(object):

    def check(self, filename):
        init()
        url = 'http://google.com'
        try:
            liner = filename.split('\n', 1)[0]
            requests.get(url, proxies={'http': 'http://' + liner}, timeout=(3.05, 27))
        except requests.exceptions.ConnectionError as e:
            return e
        except requests.exceptions.ConnectTimeout as e:
            return e
        except requests.exceptions.HTTPError as e:
            return e.code
        except requests.exceptions.Timeout as e:
            return e
        except urllib3.exceptions.ProxySchemeUnknown as e:
            return e