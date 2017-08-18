import urllib
import ctypes
import os

# from Tkinter import *
from random import randint
from time import sleep
from configparser import ConfigParser

# Pillow?


def wall_setter(res, flavour, keep, custom, custompath):

    noimage = True
    while (noimage):

        if (flavour=="NASA"):
            num = "%0.5d" % randint(0, 21000)
            url ="https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA" + num + "-" + res + ".jpg"
            # TODO: make url less random
            check = urllib.urlopen(url)
            print 'Searching...'

            if (check.getcode()!=404):
                print 'Done!'
                imgname = num + ".jpg"
                if (custom):
                    path = custompath
                else:   
                    path = os.path.dirname(os.path.realpath(__file__)) + "/papes/"
                imgpath = path + imgname

                urllib.urlretrieve(url, imgpath)

                SPI_SETDESKWALLPAPER = 20
                ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, imgpath, 3)
                if (not(keep)):
                    os.remove(imgpath)
                noimage = False

    return