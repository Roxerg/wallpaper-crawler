import urllib
import ctypes
import os

from random import randint
from time import sleep
from configparser import ConfigParser

# Pillow?


config = ConfigParser()
config.read('settings.ini')

res =  config.get('settings', 'Resolution').split('\n')[0]
flavour = config.get('settings', 'Flavour').split('\n')[0]
frequency = config.getfloat('settings', 'Change_frequency')*60
keep = config.getboolean('settings', 'Keep_used_wallpapers')
custom = config.getboolean('settings', 'Custom_save_location')
custompath = config.get('settings', 'Path').split('\n')[0]

print res
print flavour
print frequency
print keep
print custom
print custompath




noimage = True


while (noimage):

    if (flavour=="NASA"):
        num = "%0.5d" % randint(0, 21000)
        url ="https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA" + num + "-" + res + ".jpg"
        # TODO: make url less random
        check = urllib.urlopen(url)
        print check.getcode()

        if (check.getcode()!=404):
            imgname = num + ".jpg"
            if (custom):
                path = custompath
            else:   
                path = os.path.dirname(os.path.realpath(__file__)) + "/papes/"
            imgpath = path + imgname

            urllib.urlretrieve(url, imgpath)
            
            sleep(frequency)

            SPI_SETDESKWALLPAPER = 20
            ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, imgpath, 3)
            if (not(keep)):
                os.remove(imgpath)
            noimage = False


