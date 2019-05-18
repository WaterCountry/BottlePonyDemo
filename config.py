from datetime import datetime


dbfile='demo.sqlite'

def thisyear():
    return datetime.now().year

def webtitle():
    return "Bottle Pony Demo"

def basedict(way, msg):
    return dict(
        way=way,
        message=msg,
        year=thisyear(),
        appname=webtitle()
    )
