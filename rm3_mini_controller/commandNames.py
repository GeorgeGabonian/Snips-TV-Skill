#!/usr/bin/env python
# -*-: coding utf-8 -*-


import ConfigParser
from snipsremote.snipsremote import SnipsRemote
#from rm3_mini_controller import broadlink
from hermes_python.hermes import Hermes
import io
import Queue
import broadlink
import time
import re
import binascii
import os
import subprocess


#CommandName = "2ssss" #This command name has to be changed  to the user's used word
#Verification = ""
list_Of_command_Names = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero", "turn on", "turn off", "Volume up", 
                        "Volume down", "Next Channel", "Previous Channel","Menu"]
if CommandName not in list_Of_command_Names: #here you have to repeat the command name outloud to avoid mistakes. 
                print("Command not in list of commands")
		#list_Of_command_Names.append(CommandName)
                p = subprocess.Popen(['python', 'BlackBeanControl.py', '-c', CommandName])
                print("Personal Command Name should be in BB.INI")      #Transformation to  ORAL TTS FOR this one
                p.wait()
                time.sleep(20)
                if  CommandName in list_Of_command_Names:
                                print("Your Personal command has successfully been appended to your commands list")import ConfigParser
		
#		Vertification ="True"
elif CommandName in list_Of_command_Names:
                p = subprocess.Popen(['python', 'BlackBeanControl.py', '-c', CommandName])
                p.wait()
                time.sleep(7)
