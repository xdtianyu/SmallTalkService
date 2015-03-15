# SmallTalkService
SmallTalkService is a web interface for SmallTalk, it's still under development.

###Develop Dependence

```bash
apt-get install libav-tools git
pip install Flask
pip install pytz
pip install pyinstaller
pip install ansi2html
pip install sleekxmpp
pip install dnspython
```

###How to make a release

In short, just run ./build.sh.

Detail:

```bash
python server.py -g
pyinstaller server.py -F
```
This will generate a file named 'server' in dist directory. Copy file/directory server.cfg, .auto, records, statics to dist and run the follow command.

```bash
sudo -s
./server
```

Then test if everything is OK, server should run on any linux distributions.


###Author
xdtianyu@gmail.com

