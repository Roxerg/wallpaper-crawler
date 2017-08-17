import os
from configparser import ConfigParser

import urllib
import ctypes
import os

# from Tkinter import *
from random import randint
from time import sleep
from configparser import ConfigParser

# Pillow?

#local
import crawler


# Getting settings from the .ini file
config = ConfigParser()
config.read('settings.ini')

res =  config.get('settings', 'Resolution').split('\n')[0]
flavour = config.get('settings', 'Flavour').split('\n')[0]
frequency = config.getfloat('settings', 'Change_frequency')*60
keep = config.getboolean('settings', 'Keep_used_wallpapers')
custom = config.getboolean('settings', 'Custom_save_location')
custompath = config.get('settings', 'Path').split('\n')[0]
running = config.getboolean('process', 'LOOP')




print "Wallpaper Crawler 0.1. write h for help"

def main():
    raw_input(command)

    if (command == 'h'):
        print " h - this dialog"
        print " l - start or stop the loop that keeps replacing wallpaper at constant interval"
        print " s - set a new wallpaper now"
        print " q - exit (keeping the loop)"


    config = ConfigParser()
    config.read('settings.ini')
    a = config.getboolean('process', 'LOOP')



    config.set('process', 'LOOP', 'True')
    with open('settings.ini', 'w') as configfile:
        config.write(configfile)

