import requests
import time
import os
import urllib
import sys
import socket
import info
import utils
import urllib.request
from os import getcwd #done
from pathlib import Path


def checkfile():
    my_file = Path("proxylist.txt")
    if my_file.is_file():
        print('removing proxylist.txt')
        os.remove("proxylist.txt") #removing the File "proxylist.txt" to remove duplicats
        os.system('fsutil file createnew proxylist.txt 1') #creating the File "procylist.txt"
        print('creating proxylist.txt')
        pass
    else:
        os.system('fsutil file createnew proxylist.txt 1') #creating the File "procylist.txt"
        print('creating proxylist.txt')
        pass

def countproxys():
    num_lines = sum(1 for line in open('proxylist.txt')) #reading the File Lines
    print('Got {} Proxyies!'.format(num_lines)) #and Again....
    print("Sleeping 5 Secconds")


def downloadproxys():
    url1 = "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt" #url 1-4
    url2 = "https://raw.githubusercontent.com/a2u/free-proxy-list/master/free-proxy-list.txt"
    url3 = "https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt"
    url4 = "https://raw.githubusercontent.com/DarrenRainey/HTTP-Proxy-List/master/lists/1025674"
    print('downloading file 1')
    r = requests.get(url1) #request(download) 1-4
    print('downloading file 2')
    t = requests.get(url2)
    print('downloading file 3')
    l = requests.get(url3)
    print('downloading file 4')
    s = requests.get(url4)
    print('writing file 1')
    with open('proxylist.txt', 'a') as the_file:
         the_file.write(r.text) #write the Content of Download 1
    print('writing file 2')
    with open('proxylist.txt', 'a') as the_file:
         the_file.write(t.text) #write the Content of Download 2
    print('writing file 3')
    with open('proxylist.txt', 'a') as the_file:
         the_file.write(l.text) #write the Content of Download 3
    print('writing file 4')
    with open('proxylist.txt', 'a') as the_file:
         the_file.write(s.text) #write the Content of Download 4
    pass

    
