#!/usr/bin/env python
# -*-: coding utf-8 -*-

import ConfigParser
from snipsremote.snipsremote import SnipsRemote
from hermes_python.hermes import Hermes
import io
import Queue
import broadlink
import time
import re
import binascii
import os
import subprocess
from os.path import expanduser




CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"

#MQTT connection:

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


#Config.ini file parsing:


class SnipsConfigParser(ConfigParser.SafeConfigParser):
    def to_dict(self):
        return {section: {option_name : option for option_name, option in self.items(section)} for section in self.sections()}

def read_configuration_file(configuration_file):
    try:
        with io.open(configuration_file, encoding=CONFIGURATION_ENCODING_FORMAT) as f:
            conf_parser = SnipsConfigParser()
            conf_parser.readfp(f)
	    print(f)
            return conf_parser.to_dict()
    except (IOError, ConfigParser.Error) as e:
        return dict()







#Skills Intents management:


class Skill:

        def __init__(self):
            config = read_configuration_file("config.ini")



def callback(hermes, intent_message):
        pass

def remote_toggle(hermes, intent_message):
    hermes.skill.remote.toggle_on_off()

def channelup(hermes, intent_message):
    SnipsRemote.send_value("ChannelUP")

def channeldown(hermes, intent_message):
    SnipsRemote.send_value("ChannelDOWN")

#Volume Related Skills
def volumeup(hermes, intent_message):
    SnipsRemote.send_value("Volume up")
    VolumeManip.how_much_up(intent_message.slots.Numbers.first().value)

def volumedown(hermes, intent_message):
    SnipsRemote.send_value("Volume down")
    VolumeManip.how_much_down(intent_message.slots.Numbers.first().value)

def Mutebutton(hermes, intent_message):
    SnipsRemote.send_value("Mutebutton")

def turnoffon(hermes, intent_message):
    SnipsRemote.send_value("turn")

#This Skill searches for the necessary info.  and fills it in the config file.
def entering_test_mode(hermes, intent_message):
    VocalConfig.auto_setup_BlackBeanControl_ini()

#This Skill allows relearn a button if it isn't working, or if you "mis-pressed" accidentally.  
def learningmode(hermes, intent_message):
    SnipsRemote.relearn_value(intent_message.slots.button_name.first().value) 

def Menu(hermes, intent_message):
    SnipsRemote.send_value("Menu")

if __name__ == "__main__":
    with Hermes(MQTT_ADDR) as h:
       h.subscribe_intent("GabonV23:ChannelUP", channelup) \
        .subscribe_intent("GabonV23:ChannelDown", channeldown) \
        .subscribe_intent("GabonV23:ONOFF", turnoffon) \
        .subscribe_intent("GabonV23:volumedown", volumedown) \
        .subscribe_intent("GabonV23:Mutebutton",Mutebutton ) \
        .subscribe_intent("GabonV23:volumeup", volumeup) \
        .subscribe_intent("GabonV23:volumedown", volumedown) \
        .subscribe_intent("GabonV23:EnterTestMode", entering_test_mode) \
        .subscribe_intent("GabonV23:LearningMode", learningmode) \
        .subscribe_intent("GabonV23:rightbutton", rightbutton) \
        .subscribe_intent("GabonV23:leftbutton", leftbutton) \
        .subscribe_intent("GabonV23:Menu", Menu) \
        .loop_forever()
