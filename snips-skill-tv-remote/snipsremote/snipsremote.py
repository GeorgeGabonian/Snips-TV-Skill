# coding: utf8
import time
import os
from os.path import expanduser
import subprocess
import sys

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
    c= SnipsRemote(); #deleted c=
    c.go("menu")
    c.go("back")
