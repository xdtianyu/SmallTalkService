'''
    File name: singleton.py
    Author: xdtianyu@gmail.com
    Date created: 2015-03-15 12:34:57
    Date last modified: 2015-03-15 12:41:23
    Python Version: 2.7.6
'''

def singleton(class_):
  instances = {}
  def getinstance(*args, **kwargs):
    if class_ not in instances:
        instances[class_] = class_(*args, **kwargs)
    return instances[class_]
  return getinstance
