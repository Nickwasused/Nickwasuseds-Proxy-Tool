import requests
import time
import os
import urllib
import sys
import socket
import info
import utils
import urllib.request
from os import getcwd  # done
from pathlib import Path
from tqdm import tqdm


def checkfilewindows():
    my_file = Path("proxylist.txt")
    if my_file.is_file():
        print('removing proxylist.txt')
        os.remove("proxylist.txt")  # removing the File "proxylist.txt" to remove duplicats
        os.system('fsutil file createnew proxylist.txt 1')  # creating the File "procylist.txt"
        print('creating proxylist.txt')
        pass
    else:
        os.system('fsutil file createnew proxylist.txt 1')  # creating the File "procylist.txt"
        print('creating proxylist.txt')
        pass


def checkfilelinux():
    my_file = Path("proxylist.txt")
    if my_file.is_file():
        print('removing proxylist.txt')
        os.system("rm proxylist.txt")  # removing the File "proxylist.txt" to remove duplicats
        os.system('touch proxylist.txt 1')  # creating the File "procylist.txt"
        print('creating proxylist.txt')
        pass
    else:
        os.system('touch proxylist.txt')  # creating the File "procylist.txt"
        print('creating proxylist.txt')
        pass


def countproxys():
    num_lines = sum(1 for line in open('proxylist.txt'))  # reading the File Lines
    print('Got {} Proxyies!'.format(num_lines))  # and Again....
    print("Sleeping 5 Secconds")


def downloadproxys():
    chunk_size = 1024
    url1 = "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt"  # url 1-4
    url2 = "https://raw.githubusercontent.com/a2u/free-proxy-list/master/free-proxy-list.txt"
    url3 = "https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt"
    url4 = "https://raw.githubusercontent.com/DarrenRainey/HTTP-Proxy-List/master/lists/1025674"
    a = requests.get(url1, stream=True)
    b = requests.get(url2, stream=True)
    c = requests.get(url3, stream=True)
    d = requests.get(url4, stream=True)
    total_size_1 = int(a.headers['content-length'])
    total_size_2 = int(b.headers['content-length'])
    total_size_3 = int(c.headers['content-length'])
    total_size_4 = int(d.headers['content-length'])
    with open('proxylist.txt', 'wb') as f:
        for data in tqdm(iterable=a.iter_content(chunk_size=chunk_size), total=total_size_1 / chunk_size, unit='KB'):
            f.write(data)
    with open('proxylist.txt', 'wb') as f:
        for data in tqdm(iterable=b.iter_content(chunk_size=chunk_size), total=total_size_2 / chunk_size, unit='KB'):
            f.write(data)
    with open('proxylist.txt', 'wb') as f:
        for data in tqdm(iterable=c.iter_content(chunk_size=chunk_size), total=total_size_3 / chunk_size, unit='KB'):
            f.write(data)
    with open('proxylist.txt', 'wb') as f:
        for data in tqdm(iterable=d.iter_content(chunk_size=chunk_size), total=total_size_4 / chunk_size, unit='KB'):
            f.write(data)
    pass

def checkproxys():
    from checker import checker
    from colorama import Fore
    from os import system as term

    phile = 'proxylist.txt'
    filer = open(phile)
    filer = list(filer)
    checker = checker()
    for item in filer:
        if checker.check(item):
            print(Fore.RED + 'Bad proxy', item)
        else:
            phile = open('working.txt', 'a')
            phile.write(item)
    print(Fore.GREEN + 'Good proxy', item)