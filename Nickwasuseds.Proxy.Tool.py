import requests  # importing
import time
import os
import urllib
import sys
import socket
import info
import utils
import colorama
from colorama import init
from checker import checker
from colorama import Fore, Back, Style
import urllib.request
from pathlib import Path
from os import getcwd  # done

if sys.platform == 'win32':
    utils.checkfilewindows()
else:
    pass

if sys.platform == 'linux':
    utils.checkfilelinux()
else:
    pass

info.infoprint1()

utils.downloadproxys()

utils.countproxys()

time.sleep(5)  # waiting

utils.checkproxys()
