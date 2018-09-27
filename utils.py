import requests
import time
import os
import variables
import urllib
import sys
import socket
import random
import info
import utils
import urllib3
import urllib.request
from os import getcwd
from os import system as term
from pathlib import Path
from tqdm import tqdm

var = variables.urls()

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
    time.sleep(2)
    temp2 = open('proxylist.txt', 'r')
    temp3 = temp2.readline()
    num_lines = sum(1 for temp3 in temp2)
    print('Got {} Proxyies!'.format(num_lines))
    print("Sleeping 5 Secconds")
    print(" ")
    print(" ")
    print(" ")

def downloadproxys():
    chunk_size = 1000000
    url1 = var.url1
    url2 = var.url2
    url3 = var.url3
    url4 = var.url4
    a = requests.get(url1, stream=True)
    b = requests.get(url2, stream=True)
    c = requests.get(url3, stream=True)
    d = requests.get(url4, stream=True)
    total_size_1 = int(a.headers['content-length'])
    total_size_2 = int(b.headers['content-length'])
    total_size_3 = int(c.headers['content-length'])
    total_size_4 = int(d.headers['content-length'])
    with open('proxylist.txt', 'wb') as f:
        for data in tqdm(iterable=a.iter_content(chunk_size=chunk_size), total=total_size_1 / chunk_size, unit='MB'):
            f.write(data)
        for data in tqdm(iterable=b.iter_content(chunk_size=chunk_size), total=total_size_2 / chunk_size, unit='MB'):
            f.write(data)
        for data in tqdm(iterable=c.iter_content(chunk_size=chunk_size), total=total_size_3 / chunk_size, unit='MB'):
            f.write(data)
        for data in tqdm(iterable=d.iter_content(chunk_size=chunk_size), total=total_size_4 / chunk_size, unit='MB'):
            f.write(data)

def checkproxys():
    from checker import checker
    from colorama import Fore

    phile = 'proxylist.txt'
    filer = open(phile)
    filer = list(filer)
    checker = checker()
    for item in filer:
        if checker.check(item):
            temp1 = random.randint(1, 4)
            if temp1 == 1:
                print(Fore.RED + 'Bad proxy', item)
            if temp1 == 2:
                print(Fore.BLUE + 'Bad proxy', item)
            if temp1 == 3:
                print(Fore.YELLOW + 'Bad proxy', item)
            if temp1 == 4:
                print(Fore.CYAN + 'Bad proxy', item)
        else:
            phile = open('working.txt', 'a')
            phile.write(item)
            print(Fore.GREEN + 'Good proxy', item)
