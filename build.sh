#!/bin/bash

USER=$(cat /etc/passwd |grep bash| grep home|head -n1 |cut -d ':' -f 1)

if [ -z '$USER' ];then
    echo 'Error, must have a normal user!!'
    exit 0
else
    echo "Run as $USER now."
fi

if [ -d '/tmp/smalltalk' ];then
    rm -r /tmp/smalltalk
fi

sudo -u $USER mkdir /tmp/smalltalk
sudo -u $USER cp -a . /tmp/smalltalk

cd /tmp/smalltalk

echo -e "cleaning...\n"
sudo -u $USER ./clean.sh

sudo -u $USER python server.py -c server.cfg -g
sudo -u $USER pyinstaller server.py -F

if [ -f '.auto' ];then
    sudo -u $USER cp .auto dist
else 
    echo "Error, .auto file not find"
fi

if [ ! -d 'dist' ];then
    echo "Error, pyinstall failed!"
    exit 0
fi

if [ -d 'static' ];then
    sudo -u $USER cp -r static dist
else
    echo "Error, no static."
fi

if [ -f 'server.cfg' ];then
    sudo -u $USER cp server.cfg dist
fi

cd -

echo "DONE!"
