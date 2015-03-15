'''
    File name: log.py
    Author: xdtianyu@gmail.com
    Date created: 2015-03-15 13:02:20
    Date last modified: 2015-03-15 13:04:20
    Python Version: 2.7.6
'''

from time import localtime, strftime

from singleton import singleton
from config import config

@singleton
class Logger:

    def _log(self, s, color):
        time = strftime("%d/%b/%Y %H:%M:%S", localtime())
        if config.log_color:
            print("{}{} - - [{}] \"{}\"{}".format(color, config.host, time, s, bcolors.ENDC))
        else:
            print("{} - - [{}] \"{}\"".format(config.host, time, s))

    def log(self, s):
        self._log(s, bcolors.OKGREEN)
    
    def debug(self, s):
        self._log(s, bcolors.OKBLUE)
    
    def error(self, s):
        self._log(s, bcolors.FAIL)

    def info(self, s):
        if config.log_color:
            print("{} * {}{}".format(bcolors.WARNING, s, bcolors.ENDC))
        else:
            print(" * {}".format(s))

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

logger = Logger()
