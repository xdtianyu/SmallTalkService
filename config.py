'''
    File name: config.py
    Author: xdtianyu@gmail.com
    Date created: 2015-03-15 12:35:32
    Date last modified: 2015-03-15 13:04:20
    Python Version: 2.7.6
'''
import os
from singleton import singleton
import ConfigParser

@singleton
class Config():
    bin_path = './'

    host = '127.0.0.1'
    port = 8080

    xmpp_server = '127.0.0.1'
    xmpp_user = ''
    xmpp_password = ''
    
    mysql_host = ''
    mysql_database = ''
    mysql_user = ''
    mysql_pass = ''

    debug = False
    log_color = False


    def load(self, config):
        if not os.path.isfile(config):
            print " * Error parsing config: FILE NOT EXIST. Using default config."
        else:
            conf = ConfigParser.ConfigParser()
            conf.read(config)
            
            self.host = conf.get('server', 'host')
            self.port = conf.getint('server', 'port')
            
            self.xmpp_server = conf.get('xmpp', 'xmpp_server')
            self.xmpp_user = conf.get('xmpp', 'xmpp_user')
            self.xmpp_password = conf.get('xmpp', 'xmpp_password')
            
            self.mysql_host = conf.get('mysql', 'mysql_host')
            self.mysql_database = conf.get('mysql', 'mysql_database')
            self.mysql_user = conf.get('mysql', 'mysql_user')
            self.mysql_pass = conf.get('mysql', 'mysql_pass')

            self.debug = conf.getboolean('extra', 'debug')
            self.log_color = conf.getboolean('extra', 'log_color')

config = Config();
