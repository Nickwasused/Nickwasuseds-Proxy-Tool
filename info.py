import colorama
import utils
import variables
from colorama import init
from colorama import Fore, Style

init()


def infoprint1():
    init()
    print(Style.BRIGHT + '  ')
    print(Fore.RED + 'Made by Nickwasused')
    print(Fore.BLUE + '************************')
    print(Fore.GREEN + 'Version: 1.0.2')
    print(Fore.RED + 'Sources for Proxy Servers:')
    print(Fore.YELLOW + variables.urls.url1)
    print(Fore.BLUE + variables.urls.url2)
    print(Fore.GREEN + variables.urls.url3)
    print(Fore.RED + variables.urls.url4)
    print(' ')
