#!/bin/python
from os import system; from platform import system as sm
stm: str = str(sm())
if 'linux' in stm.lower() or 'mac' in stm.lower():
    s = system ('ls > data0101.txt')
    if '0' in str(s):
        print('\n\033[92myour linux system!\n')
    else:
        print('\033[31m[!] \033[36myour system is pydroid or not root, please run in linux system or command \'sudo su\' thanks')
        quit ()
    try:
        file_ = open('data0101.txt', 'r+').read()
    except:
        print('\033[31m[!] \033[36myour system is pydroid or not root, please run in linux system or command \'sudo su\' thanks')
        quit ()
   if 'hack-rubika' in file_:
        system('cd hack-rubika && chmod 777 * && python3 hack-rubika.py')
    else:
        system('rm -rf hack-rubika')
        system('git clone https://github.com/mester-root/hack-rubika')
        system ('cd hack-rubika')
        system ('python3 hack-rubika.py')
else:
    print('\n\033[31m[\033[36mgithun.com/mester-root/hack-rubika\033[31m]\n')
