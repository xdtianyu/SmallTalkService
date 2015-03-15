'''
    File name: login.py
    Author: xdtianyu@gmail.com
    Date created: 2015-02-18 20:20:59
    Date last modified: 2015-03-15 12:41:23
    Python Version: 2.7.6
'''

from flask import jsonify

def post(request, mysql):
    username = request.form['username']
    password = request.form['password']
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from user where username='"+ username + "' and password= '" + password + "'")
    data = cursor.fetchone()
    if data is None:
        return jsonify(result="failed", message="Username or Password is wrong")
    else:
        return jsonify(result="succeed", message="Logged in successfully")

def show_login():
    return "login";
