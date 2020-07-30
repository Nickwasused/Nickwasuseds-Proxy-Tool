#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Source Code: https://github.com/pythonism/proxy-checker

import requests
import urllib3

class Checker(object):

    def check(self, filename):
        url = 'https://www.cloudflare.com/'
        try:
            liner = filename.split('\n', 1)[0]
            requests.get(url, proxies={'http': 'http://' + liner}, timeout=(2))
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
