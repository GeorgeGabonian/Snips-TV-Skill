#!/usr/bin/python
# coding: utf8
import time
import os
from os.path import expanduser
import subprocess
import sys
from configparser import ConfigParser
import broadlink 
import re
import binascii




Config = ConfigParser()
Config.optionxform = str

class VocalConfig:
        def __init__(self):
            pass

        @staticmethod
        def auto_setup_BBC_ini():
                print('Scanning network for Broadlink devices (5s timeout) ... ')
                devices = broadlink.discover(timeout=5)
                print(('Found ' + str(len(devices )) + ' broadlink device(s)'))
                time.sleep(1)
                for index, item in enumerate(devices):
                        devices[index].auth()
                m = re.match(r"\('([0-9.]+)', ([0-9]+)", str(devices[index].host))
                ipadd = m.group(1)
                port = m.group(2)
                macadd = str(''.join(format(x, '02x') for x in devices[index].mac[::-1]))
                macadd = macadd[:2] + ":" + macadd[2:4] + ":" + macadd[4:6] + ":" + macadd[6:8] + ":" + macadd[8:10] + ":" + macadd[10:12]
                print(('Device ' + str(index + 1) +':\nIPAddress = ' + ipadd + '\nPort = ' + port + '\nMACAddress = ' + macadd))




                Config['General'] = {
                                "IPAddress":ipadd,
                                'Port':port,
                                'MACAddress':macadd,
                                'Timeout':'20'
                }
                Config['Commands'] = {
                }
                os.chdir("/home/pi/rm3_mini_controller/")
                with open('BlackBeanControl.ini','w') as f:
                        Config.write(f)
                        f.close()







class SnipsRemote:
    @classmethod
    def __init__(self, locale = "EN_US"):
        pass

    @staticmethod
    def send_value(s):
        if (s is None or s == ""):
            return
        dir = expanduser("/home/pi") + u'/rm3_mini_controller/'
        if (not os.path.isdir(dir)):
            return
            print(text_value)
        p = subprocess.Popen(['python', u'BlackBeanControl.py', '-c', s], cwd=dir)
        p.wait()
        time.sleep(20)

    @staticmethod
    def rekey_value(s):
        if (s is None or s == ""):
            return
        dir = expanduser("/home/pi") + u'/rm3_mini_controller/'
        if (not os.path.isdir(dir)):
            return
            print(text_value)
        p = subprocess.Popen(['python', u'BlackBeanControl.py', '-r', s], cwd=dir)
        p.wait()
        time.sleep(20)


if (__name__ == "__main__"):
    SnipsRemote();
    
