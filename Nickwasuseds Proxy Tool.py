import requests
import time
import os
from os import getcwd

print('Made by Nickwasused')
print('*******************')
print('Version: 0.4')
print('Sources for Proxy Servers:')
print('https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt')
print('https://raw.githubusercontent.com/a2u/free-proxy-list/master/free-proxy-list.txt')
print('https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list')
print('https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt')
os.system('fsutil file createnew proxylist.txt 1')
os.remove("proxylist.txt")
url1 = "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt"
url2 = "https://raw.githubusercontent.com/a2u/free-proxy-list/master/free-proxy-list.txt"
url3 = "https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list"
url4 = "https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt"
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
    the_file.write(url4)
print('got this:')
print(r.text)
print(t.text)
print(l.text)
print(s.text)

