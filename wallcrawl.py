import urllib
import ctypes
import os
import multiprocessing

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


def looper(file, running, res, flavour, keep, custom, custompath):
    while (running):
        config.read('settings.ini')
        running = config.getboolean('process', 'LOOP')
        crawler.wall_setter(res, flavour, keep, custom, custompath)
        sleep(frequency)
    

def main():

    command = ''
    command = raw_input(">> ")

    if (command == 'h'):
        print """ 
        edit the settings.ini file to choose whether to
        save used wallpapers,where to save them, how 
        frequently should the wallpapers change, what 
        should their resolution be and what type of 
        wallpaper you want (currently only 1 choice)

            """
        print "    h - this dialog"
        print "    l - start or stop the loop that keeps replacing wallpapers"
        print "    s - set a new wallpaper now"
        print "    q - exit"


    elif (command == 'l'):

        running = config.getboolean('process', 'LOOP')

        if (running):
            print "Disabled!"
            config.set('process', 'LOOP', 'False')
        else: 
            print "Enabled!"
            config.set('process', 'LOOP', 'True')
        
        with open('settings.ini', 'w') as configfile:
            config.write(configfile)
            
        os.system("wallcrawlloop.pyw")

    elif (command == 's'):
        crawler.wall_setter(res, flavour, keep, custom, custompath)

    elif (command == 'q'):
        print "Bye!"
        sleep(0.5)
        return

    main()


print "Wallpaper Crawler 0.1. write h for help"
main()



