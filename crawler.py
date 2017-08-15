import random
import urllib
import ctypes
# Pillow?
import os

noimage = True
while (noimage):
    num = "%0.5d" % random.randint(0, 21000)
    res = "1920x1200"  # make adjustable res
    url ="https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA" + num + "-" + res + ".jpg"
    # TODO: make url less random
    check = urllib.urlopen(url)
    print check.getcode()

    if (check.getcode()!=404):
        imgname = num + ".jpg"
        path = os.path.dirname(os.path.realpath(__file__)) + "/papes/"
        imgpath = path + imgname
        urllib.urlretrieve(url, imgpath)
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, imgpath, 3)
        noimage = False


