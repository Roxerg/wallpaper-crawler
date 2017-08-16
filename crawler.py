import urllib
import ctypes
import os

from random import randint
from time import sleep

# Pillow?


setfile = open('settings.txt', "r")
settings = setfile.readlines()
setfile.close()

res = settings[0][13:].split('\n')[0]
flavour = settings[7][10:].split('\n')[0]
frequency = float(settings[13][19:])*60
keep = bool(int(settings[18][23:]))
custom = bool(int(settings[20][23:]))
custompath = settings[21][7:].split('\n')[0]

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


