import requests
import time
import os
import urllib
import sys
import socket
import ctypes
import urllib.request
import colorama
from colorama import init
from colorama import Fore, Back, Style
from os import getcwd

init()
ctypes.windll.kernel32.SetConsoleTitleW("Nickwasused´s Proxy Tool")
print(Fore.RED + 'Made by Nickwasused')
print(Fore.RED + '************************')
print(Fore.GREEN + 'Version: 0.7')
print(Fore.WHITE + 'Sources for Proxy Servers:')
print(Back.BLUE + 'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt')
print(Back.BLUE + 'https://raw.githubusercontent.com/a2u/free-proxy-list/master/free-proxy-list.txt')
print(Back.BLUE + 'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt')
print(Back.BLUE + 'https://raw.githubusercontent.com/DarrenRainey/HTTP-Proxy-List/master/lists/1025674')
os.system('fsutil file createnew proxylist.txt 1')
os.remove("proxylist.txt")
url1 = "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt"
url2 = "https://raw.githubusercontent.com/a2u/free-proxy-list/master/free-proxy-list.txt"
url3 = "https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt"
url4 = "https://raw.githubusercontent.com/DarrenRainey/HTTP-Proxy-List/master/lists/1025674"
directory = getcwd()
filename = directory + 'proxylist.txt'
r = requests.get(url1)
t = requests.get(url2)
l = requests.get(url3)
s = requests.get(url4)
with open('proxylist.txt', 'a') as the_file:
    the_file.write('***********************************************')
with open('proxylist.txt', 'a') as the_file:
    the_file.write('Proxy List generated by Nickwasuseds Proxy Tool')
with open('proxylist.txt', 'a') as the_file:
    the_file.write('***********************************************')
with open('proxylist.txt', 'a') as the_file:
    the_file.write(r.text)
with open('proxylist.txt', 'a') as the_file:
    the_file.write(t.text)
with open('proxylist.txt', 'a') as the_file:
    the_file.write(l.text)
with open('proxylist.txt', 'a') as the_file:
    the_file.write(s.text)
with open('proxylist.txt', 'a') as the_file:
    the_file.write(url1)
with open('proxylist.txt', 'a') as the_file:
    the_file.write(url2)
with open('proxylist.txt', 'a') as the_file:
    the_file.write(url3)
with open('proxylist.txt', 'a') as the_file:
    the_file.write(url3)
print(Back.YELLOW + '')
num_lines = sum(1 for line in open('proxylist.txt'))
print('Got {} Proxyies!'.format(num_lines))
print(Fore.WHITE + "Sleeping 5 Secconds")
time.sleep(5)
proxys  = open('proxylist.txt', 'r')
proxyList = proxys.readlines()
try:
        proxies = {"http": "http://" + str(proxyList)}
        opener = urllib.request.FancyURLopener(proxies)
        opener.open("https://www.google.com")
except IOError:
    print(Fore.RED + "Proxy error! (Check proxy)")
    time.sleep(5)
else:
    print(Fore.GREEN + "All proxies are Working!")
    time.sleep(5)
