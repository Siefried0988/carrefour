import configparser as cp
import os

def config():
    currentPath = os.path.dirname(os.path.realpath(__file__))
    path = currentPath + '\\config.ini'

    print(path)
    inifile = cp.ConfigParser()
    inifile.read(path, 'UTF-8')
    return inifile


#print('fuzz.name = ', inifile.get('fuzz', 'name'))

