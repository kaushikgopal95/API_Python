import configparser


def getconfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config
