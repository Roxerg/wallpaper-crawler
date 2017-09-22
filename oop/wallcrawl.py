import urllib
import ctypes
import os
#import multiprocessing
#import re

from sys import platform

# from Tkinter import *
from random import randint
from time import sleep
from configparser import ConfigParser

# Pillow?

class Wall:

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
    imgpath = ""


    def looper(self):
        while (self.running):
            self.config.read('settings.ini')
            running = self.config.getboolean('process', 'LOOP')
            self.wall_setter()
            sleep(self.frequency)

    def wall_setter(self):

        noimage = True
        self.downloader()
        self.wallpapersetter()

        return

    def downloader(self):

        # TODO: this whole thing
        if (self.flavour=="NASAsite"):
            noimage = True
            while (noimage):
                num = "%0.5d" % randint(0, 21000)
                url ="https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA" + num + "-" + self.res + ".jpg"
                # TODO: make url less random
                check = urllib.urlopen(url)
                print 'Searching...'

                if (check.getcode()!=404):
                    print 'Done!'
                    imgname = num + ".jpg"
                    if (self.custom):
                        path = self.custompath
                    else:   
                        path = os.path.dirname(os.path.realpath(__file__)) + "/papes/"
                    imgpath = path + imgname

                    urllib.urlretrieve(url, imgpath)

                    noimage = False
                    self.imgpath = imgpath
                    print self.imgpath



        elif (self.flavour=="4chan"):
                #flavour =  re.sub(r'[^a-zA-Z0-9\s]+', '', title).replace(" ", "-")
                print "Not implemented... "
                sleep(2)
                print "...yet!"

    def wallpapersetter(self):

        if platform.startswith("win"):
            SPI_SETDESKWALLPAPER = 20
            ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, self.imgpath, 3)
        elif platform.startswith("linux"):
            import gconf
            envir = os.environ.get('DESKTOP_SESSION')
            #https://stackoverflow.com/a/21213358/8439299




            conf = gconf.client_get_default()
            gnomepath = "/desktop/gnome/background/currentwall.jpg" 
            conf.set_string(gnomepath, self.imgpath)
        elif platform.startswith("darwin"):
            import subprocess

            SCRIPT = """/usr/bin/osascript<<END
                        tell application "Finder"
                        set desktop picture to POSIX file "%s"
                        end tell
                        END"""

            subprocess.Popen(SCRIPT%self.imgpath, shell=True)

        if (not(self.keep)):
            os.remove(self.imgpath)


    


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
        print "    l - toggle loop"
        print "    la - launch loop, making you not able to enter commands cuz i suck"
        print "    s - set a new wallpaper now"
        print "    q - exit"


    elif (command == 'l'):

        running = Wall.config.getboolean('process', 'LOOP')

        if (running):
            print "Disabled!"
            Wall.config.set('process', 'LOOP', 'False')
        else: 
            print "Enabled!"
            Wall.config.set('process', 'LOOP', 'True')
        
        with open('settings.ini', 'w') as configfile:
            Wall.config.write(configfile)
            

    elif (command == 'la'):
        os.system("wallcrawlloop.pyw")

    elif (command == 's'):
        WallObject = Wall()
        WallObject.wall_setter()

    elif (command == 'q'):
        print "Bye!"
        sleep(0.5)
        return

    main()

if __name__ == "__main__":
    print "Wallpaper Crawler 0.1. write h for help"
    main()







