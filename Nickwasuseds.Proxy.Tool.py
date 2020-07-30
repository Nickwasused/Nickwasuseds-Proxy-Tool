import os
import sys
import time
import requests
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

url1 = 'https://raw.githubusercontent.com/a2u/free-proxy-list/master/free-proxy-list.txt'
url2 = 'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt'
url3 = 'https://raw.githubusercontent.com/DarrenRainey/HTTP-Proxy-List/master/lists/proxy-list'
url4 = 'http://multiproxy.org/txt_all/proxy.txt'

temp1 = 'temp1.txt'
temp2 = 'temp2.txt'
temp3 = 'temp3.txt'
temp4 = 'temp4.txt'

proxyfile = 'proxylist.txt'
workingfile = 'working.txt'

create = 'creating {}'
remove = 'removing {}'

def checkfilewindows(file):
    my_file = file
    if os.path.exists(my_file):
        print(remove.format(my_file))
        os.remove(my_file)  # removing the File "proxylist.txt" to remove duplicats
        with open(my_file, 'w+') as my_file:
            my_file.close() # creating the File "procylist.txt"
        print(create.format(my_file))
    else:
        os.system('fsutil file createnew {} 1'.format(my_file))  # creating the File "procylist.txt"
        print(create.format(my_file))

def checkfilelinux(file):
    my_file = file
    if os.path.exists(my_file):
        print('removing {}'.format(my_file))
        os.remove(my_file)  # removing the File "proxylist.txt" to remove duplicats
        with open(my_file, 'w+') as my_file:
            my_file.close() # creating the File "proxylist.txt"
        print(create.format(my_file))
    else:
        os.system('touch {}'.format(my_file))  # creating the File "proxylist.txt"
        print(create.format(my_file))

def mergefiles():
    filenames = [temp1, temp2, temp3, temp4]
    with open(proxyfile, 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)

def cleanup():
    os.remove(temp1)
    os.remove(temp2)
    os.remove(temp3)
    os.remove(temp4)


def countproxys():
    time.sleep(2)
    num_lines = sum(1 for _ in open(proxyfile, 'r'))
    print('Got {} Proxys!'.format(num_lines))
    print("Sleeping 5 Seconds")
    print(" ")
    print(" ")
    print(" ")

def downloadproxy(url, filename):
    chunk_size = 1000000
    a = requests.get(url, stream=True)
    total_size_1 = int(a.headers['content-length'])
    with open(filename, 'wb') as f:
        for data in tqdm(iterable=a.iter_content(chunk_size=chunk_size), total=total_size_1 / chunk_size, unit='MB'):
            f.write(data)

def checkproxys():
    from checker import Checker

    proxylist = open(proxyfile)
    proxylist = list(proxylist)
    checker = Checker()
    for item in proxylist:
        if checker.check(item):
            continue
        else:
            output = open(workingfile, 'a')
            output.write(item)

if sys.platform == 'win32':
    print('System: Windows')
    checkfilewindows(proxyfile)
    checkfilewindows(temp1)
    checkfilewindows(temp2)
    checkfilewindows(temp3)
    checkfilewindows(temp4)

if sys.platform == 'linux':
    print('System: Linux')
    checkfilelinux(proxyfile)
    checkfilelinux(temp1)
    checkfilelinux(temp2)
    checkfilelinux(temp3)
    checkfilelinux(temp4)


with ThreadPoolExecutor(max_workers=5) as executor:
    for x in range(1, 5):
        url = globals()['url{}'.format(x)]
        print(url)
        filename = 'temp{}.txt'.format(x)
        executor.submit(downloadproxy(url, filename))

mergefiles()

cleanup()

countproxys()

with ThreadPoolExecutor(max_workers=8) as executor:
    for x in range(1, 9):
        executor.submit(checkproxys())