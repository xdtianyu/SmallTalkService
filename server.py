'''
    File name: server.py
    Author: xdtianyu@gmail.com
    Date created: 2015-01-25 09:56:23
    Date last modified: 2015-03-15 13:07:50
    Python Version: 2.7.3
'''

from flask import Flask
from flask import request
from flaskext.mysql import MySQL

from config import config

import os.path
import sys
import getopt


import index
import login

mysql = MySQL()
app = Flask(__name__, static_url_path="/static")


@app.route("/")
def root():
    return index.show_index()

@app.route("/login", methods=["GET","POST"])
def show_control():
    if request.method == "POST":
        return login.post(request, mysql)
    else:
        return login.show_login()

if __name__ == '__main__':
    config.bin_path = os.path.realpath(os.path.dirname(sys.argv[0]))
    config_file = config.bin_path+'/server.cfg'
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hc:g", ["help", "config=", "generate"])
    except getopt.GetoptError:
        print ' Usage: server.py -c <config file>'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print ' Usage: server.py -c <config file>'
            sys.exit()
        elif opt in ("-c", "--config"):
            config_file = arg
        elif opt in ("-g", "--generate"):
            config.load(config_file)
            #about.version()
            sys.exit()

    config.load(config_file)


    app.config['MYSQL_DATABASE_USER'] = config.mysql_user
    app.config['MYSQL_DATABASE_PASSWORD'] = config.mysql_pass
    app.config['MYSQL_DATABASE_DB'] = config.mysql_database
    app.config['MYSQL_DATABASE_HOST'] = config.mysql_host
    mysql.init_app(app)

    app.run(debug=config.debug, host=config.host, port=config.port)
