from wallcrawl import Wall

from time import sleep
from configparser import ConfigParser

config = ConfigParser()
config.read('settings.ini')
running = config.getboolean('process', 'LOOP')
WallObject = Wall()

while (running):
    config.read('settings.ini')
    running = config.getboolean('process', 'LOOP')
    if (running):
        print "set!"
        WallObject.wall_setter()
        sleep(Wall.frequency)



