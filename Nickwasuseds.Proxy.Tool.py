import requests #importing
import time
import os
import urllib
import sys
import socket
import ctypes
import NickwasusedPrint
import urllib.request
import colorama
from pathlib import Path
from colorama import init
from colorama import Fore, Back, Style
from os import getcwd #done

NickwasusedPrint.versiontxt()

f=open('version.txt') #reading the version file
lines=f.readlines()

print(Fore.RED + 'Made by Nickwasused') #printing some stuff
print(Fore.RED + '************************')
print(Fore.GREEN + 'Version:')
version = print(lines[0]) #reading version Line
print(version)
print(Fore.WHITE + 'Sources for Proxy Servers:')
print(Back.BLUE + 'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt')
print(Back.BLUE + 'https://raw.githubusercontent.com/a2u/free-proxy-list/master/free-proxy-list.txt')
print(Back.BLUE + 'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt')
print(Back.BLUE + 'https://raw.githubusercontent.com/DarrenRainey/HTTP-Proxy-List/master/lists/1025674') #end printing


with open('version.txt') as myfile:
    if 'wjkjwkbndjkawjkdnjwadnjka' in myfile.read():
         print('Update avalible here: https://github.com/Nickwasused/Nickwasuseds-Proxy-Tool')
    else:
        pass

init() #init colorrama

ctypes.windll.kernel32.SetConsoleTitleW("Nickwasused´s Proxy Tool") #setting the Window Title

my_file = Path("proxylist.txt")
if my_file.is_file():
    os.remove("proxylist.txt") #removing the File "proxylist.txt" to remove duplicats
else:
    os.system('fsutil file createnew proxylist.txt 1') #creating the File "procylist.txt"

NickwasusedPrint.getproxy()

num_lines = sum(1 for line in open('proxylist.txt')) #reading the File Lines

print('Got {} Proxyies!'.format(num_lines)) #and Again....
print(Fore.WHITE + "Sleeping 5 Secconds")

time.sleep(5) #waiting

