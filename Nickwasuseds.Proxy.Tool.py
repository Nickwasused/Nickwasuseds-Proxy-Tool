import requests  # importing
import time
import os
import urllib
import sys
import socket
import multiprocessing
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


worker_0 = multiprocessing.Process(
    name='worker 0',
    target=utils.downloadproxy1(),
)

worker_1 = multiprocessing.Process(
    name='worker 1',
    target=utils.downloadproxy2(),
)

worker_2 = multiprocessing.Process(
    name='worker 2',
    target=utils.downloadproxy3(),
)

worker_3 = multiprocessing.Process(
    name='worker 3',
    target=utils.downloadproxy4(),
)

worker_0.start()
worker_1.start()
worker_2.start()
worker_3.start()

utils.countproxys()

time.sleep(5)  # waiting

worker_4 = multiprocessing.Process(
    name='worker 4',
    target=utils.checkproxys(),
)

worker_5 = multiprocessing.Process(
    name='worker 5',
    target=utils.checkproxys(),
)

worker_6 = multiprocessing.Process(
    name='worker 6',
    target=utils.checkproxys(),
)

worker_7 = multiprocessing.Process(
    name='worker 7',
    target=utils.checkproxys(),
)

worker_4.start()
worker_5.start()
worker_6.start()
worker_7.start()
