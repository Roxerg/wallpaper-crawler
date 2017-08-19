import crawler

from time import sleep
from configparser import ConfigParser

config = ConfigParser()
config.read('settings.ini')

res =  config.get('settings', 'Resolution').split('\n')[0]
flavour = config.get('settings', 'Flavour').split('\n')[0]
frequency = config.getfloat('settings', 'Change_frequency')*60
keep = config.getboolean('settings', 'Keep_used_wallpapers')
custom = config.getboolean('settings', 'Custom_save_location')
custompath = config.get('settings', 'Path').split('\n')[0]
running = config.getboolean('process', 'LOOP')


while (running):
    config.read('settings.ini')
    running = config.getboolean('process', 'LOOP')
    crawler.wall_setter(res, flavour, keep, custom, custompath)
    sleep(frequency)



