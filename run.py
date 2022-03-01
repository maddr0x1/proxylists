
import requests
from bs4 import BeautifulSoup as bs
import colorama
from colorama import Fore
import os
import read
import sys
from time import sleep
import pyperclip as py
import write
import datetime
import pandas as pd


text = "\033[0;91m[+] This program will scrape (Http(s),Socks4,Socks5) proxies into separate files"


sleep(0.01)  # In seconds        sys.stdout.write(x)
sys.stdout.flush()
print(text)

proxies = int(input("""\033[0;37m
[+] Which type of proxy do you need?

[1] Http/Https
[2] Socks4
[3] Socks5
[4] DEVTEST


       \n
[Enter a No. (1-4) ]> """))


if proxies == 1:
    print('Scraping in progress')
    print('.')
    print('.')
    print('.')
    proxy_url = 'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http%2Bhttps.txt'
    local_file = 'HTTP_HTTPS_LIST.txt'
    r = requests.get(proxy_url)
    with open(local_file, 'wb')as a_file:
        a_file.write(r.content)
        py.copy(r.text)
        a_file.close()
    with open(local_file, 'r')as a_file:
        num_lines = sum(1 for line in a_file if line.rstrip())
        a_file.close()
    print(
        'Process complete!', num_lines, ' proxies have been saved to the appropriately titled txt file in the directory, as well as copied to your clipboard!')
    sleep(2)
    input('+++PRESS ANY KEY TO EXIT+++')
    sys.exit(input)

if proxies == 2:
    proxy_url = 'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt'
    local_file = 'SOCKS4_LIST.txt'
    r = requests.get(proxy_url)
    with open(local_file, 'wb') as a_file:
        a_file.write(r.content)
        py.copy(r.text)
        a_file.close()
    with open(local_file, 'r') as a_file:
        num_lines = sum(1 for line in a_file if line.rstrip())
        a_file.close()

        print(
            'Process complete!', num_lines,
            ' proxies have been saved to the appropriately titled txt file in the directory, as well as copied to your clipboard!')
        sleep(2)
        input('+++PRESS ANY KEY TO EXIT+++')
        sys.exit(input)


if proxies == 3:
    proxy_url = 'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt'
    local_file = 'SOCKS5_LIST.txt'
    r = requests.get(proxy_url)
    with open(local_file, 'wb') as a_file:
        a_file.write(r.content)
        py.copy(r.text)
        a_file.close()
    with open(local_file, 'r') as a_file:
        num_lines = sum(1 for line in a_file if line.rstrip())
        a_file.close()

        print(
            'Process complete!', num_lines,
            ' proxies have been saved to the appropriately titled txt file in the directory, as well as copied to your clipboard!')
        sleep(2)
        input('+++PRESS ANY KEY TO EXIT+++')
        sys.exit(input)




