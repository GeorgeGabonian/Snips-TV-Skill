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
        #getting and assigning your Broadlink's IP & MAC addresses + port vocally.
        @staticmethod
        def auto_setup_BlackBeanControl_ini():
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
        time.sleep(1.2)


    #I excluded rekeying, since I realized relean_value could be used instead. However, I did not delete it entirely 'cause some people may have to use it.
    """@staticmethod
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
   """

    @staticmethod
    def relearn_value(The_name_of_the_button):

        #Turning on Learning Mode:
        print("enter_learning (5s timeout) please press any key on remote to test")
        devices = broadlink.discover(timeout=5)
        for index, item in enumerate(devices):
                devices[index].auth()
        devices[0].enter_learning()
        time.sleep(7)
        print("Check data")
        ir_packet = devices[0].check_data()
        if ir_packet:
                decode_command = binascii.hexlify(ir_packet).decode("ascii")
                print(decode_command)
                encode_command = binascii.unhexlify(decode_command)
                devices[0].send_data(encode_command) #Retesting if it works.
                print("Test resend")
        else:
                print("RM3 not receive any remote command")

        #Replacing the former option's key in the config file
        os.chdir("/home/pi/rm3_mini_controller/")
        with open('BlackBeanControl.ini','r+') as f:
                print('in the file')
                print(Config.read('BlackBeanControl.ini'))
                print(Config.options('Commands'))
                Config.set("Commands", The_name_of_the_button, decode_command)
                Config.write(f)
                f.close()



class VolumeManip:
        def __init__(self):
                pass

        #I seperated them for legibility purposes.
        @staticmethod
        def how_much_up(the_number_to_iterate):
                for i in range (0,int(the_number_to_iterate)):
                        SnipsRemote.send_value("Volume up")

        @staticmethod
        def how_much_down(the_number_to_iterate):
                for i in range (0,int(the_number_to_iterate)):
                        SnipsRemote.send_value("Volume down")





if (__name__ == "__main__"):
     SnipsRemote();
