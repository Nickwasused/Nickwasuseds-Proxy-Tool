import requests #importing
import time
import os
import urllib
import sys
import socket
import info
import utils
import colorama
from colorama import init
from colorama import Fore, Back, Style
import urllib.request
from pathlib import Path
from os import getcwd #done

info.infoprint1()

utils.checkfile()

utils.downloadproxys()

utils.countproxys()

time.sleep(5) #waiting

