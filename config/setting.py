import logging.config
import configparser
import os

CONFIG_FILE_PART =  '/home/user/PycharmProjects/python_dns/config/config.ini'
def get_param(name):
    conf  = os.environ.get(name)
    if conf:
        return conf
    else :
        config = configparser.ConfigParser()
        try:
            config.read(CONFIG_FILE_PART)
            return config['SETTING'][name]
        except Exception :
            config.read(os.environ.get('DNS_PATH_SETTING'))
            return config['SETTING'][name]

