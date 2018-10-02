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




#Changing DIR to parse registered commands:

"""os.chdir("/home/pi/rm3_mini_controller/")

CONFIGURATION_ENCODING_FORMAT = "utf-8"
BlackBeanControl_INI = "BlackBeanControl.ini"
the_commands_dictionary = {}
class SnipsConfigParsertwo(ConfigParser.SafeConfigParser):
    def to_dict(self):
        return {section: {option_name : option for option_name, option in self.items(section)} for section in self.sections()}


def read_configuration_file2(configuration_file):
    try:
        with io.open(configuration_file, encoding=CONFIGURATION_ENCODING_FORMAT) as f:
            
	    conf_parser = SnipsConfigParsertwo()
            conf_parser.readfp(f)
	    print(f)
            return conf_parser.to_dict()
    except (IOError, ConfigParser.Error) as e:
        return dict()
#I have 2 write another function write_configg_file
def write_configuration_file(intent_message):
   configuration_file_name = "/home/pi/rm3_mini_controller/BlackBeanControl.ini" 
   theCommandFile = read_configuration_file2(configuration_file_name)
   with io.open(configuration_file_name, "w+") as f:
       #for r in intent_message.slots.button_name:
          if intent_message.slots.button_name.first().value.lower() in theCommandFile.get('Commands').keys():
		    del ['theCommandFile.intent_message.slots.button_name.first().value.lower()']
#f.write.key.value = "blabla"
"""







###########################################Back to SKILL DIR
#os.chdir("/home/pi/snips-skill-tv-remote/")



CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"

#MQTT connection

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


#Config.ini file parsing


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







#Skills Intents management.


class Skill:

	def __init__(self):
            config = read_configuration_file("config.ini")
            extra = config["global"].get("extra", False)
            self.coffee = CoffeeHack(extra = extra)

def extract_coffee_size(intent_message):
    res = []
    if intent_message.slots.coffee_size is not None:
        for r in intent_message.slots.coffee_size:
            res.append(r.slot_value.value.value)
    return res

def callback(hermes, intent_message):
    t = extract_coffee_type(intent_message)
    s = extract_coffee_size(intent_message)
    ta = extract_coffee_taste(intent_message)
    n = extract_coffee_number(intent_message)
    button_name = ""
    coffee_size = ""
    coffee_taste = ""
    number = 1
    if len(t):
        coffee_type = t[0]
    if len(s):
        coffee_size = s[0]
    if len(ta):
        coffee_taste = ta[0]
    if len(n):
        try:
            number = int(n[0])
        except ValueError, e:
            number = 2
    print(t)
    print(s)
    print(ta)
    hermes.skill.coffee.pour(coffee_type = coffee_type,
                coffee_size = coffee_size,
                coffee_taste = coffee_taste,
                number = number)

def remote_toggle(hermes, intent_message):
    hermes.skill.remote.toggle_on_off()


def channelup(hermes, intent_message):
    print("intent subscribed")
    SnipsRemote.send_value("ChannelUP")
    print("value sent")

def channeldown(hermes, intent_message):
    SnipsRemote.send_value("ChannelDOWN")

def volumeup(hermes, intent_message):
    SnipsRemote.send_value("Volume up")

def turnoffon(hermes, intent_message):
    SnipsRemote.send_value("turnoffon")

def learningmode(hermes, intent_message):
    if intent_message.slots.button_name is not None:
            for r in intent_message.slots.button_name:
                SnipsRemote.send_value(r.slot_value.value.value) 
#    else:
        #TTS to say choose your button:
        #time.sleep(20) to continue session:
#       for r in intent_message.slots.button_name:
#                SnipsRemote.send_value(r.slot_value.value.value)


"""    configuration_file_name = "/home/pi/rm3_mini_controller/BlackBeanControl.ini" 

    # TODO : Parse ini file 
    theCommandFile = read_configuration_file2(configuration_file_name) #a la place de read voir s'il ya write 
    print theCommandFile
#    write_configuration_file("intent_message") # END 

    theCommandFile_get_Commands = theCommandFile.get('Commands') #enlever
    print theCommandFile.get('Commands')

    print intent_message.slots.button_name.first().value
    for r in intent_message.slots.button_name:
       if intent_message.slots.button_name.first().value.lower() in theCommandFile.get('Commands').keys():
	   print("yes it is")
	   theCommandFile['Commands'][intent_message.slots.button_name.first().value] = "SnipsRemote.send_value(r.slot_value.value.value)"
	   print("yes it is")
	   # print SnipsRemote.send_value(r.slot_value.value.value)
	   #print theCommandFile['Commands'][intent_message.slots.button_name.first().value]


#	    for intent in intent_message.slots.button_name:
	    #tts this key will be rekeyed
	    #SnipsRemote.rekey_value(intent.slot_value.value.value)
    if intent_message.slots.button_name is not None:
            for r in intent_message.slots.button_name:
                SnipsRemote.send_value(r.slot_value.value.value) 
    else:
        #TTS to say choose your button:
	#time.sleep(20) to continue session:
	    for r in intent_message.slots.button_name:
                SnipsRemote.send_value(r.slot_value.value.value)"""

if __name__ == "__main__":
    with Hermes(MQTT_ADDR) as h:
       h.subscribe_intent("GabonV23:ChannelUP", channelup) \
        .subscribe_intent("GabonV23:ChannelDown", channeldown) \
	.subscribe_intent("GabonV23:ONOFF", turnoffon) \
	.subscribe_intent("GabonV23:volumeup", volumeup) \
	.subscribe_intent("GabonV23:LearningMode", learningmode) \
        .loop_forever()
