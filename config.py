from datetime import datetime


dbfile='demo.sqlite'
faviconico='/static/images/book.gif'

def thisyear():
    return datetime.now().year

def webtitle():
    return "Bottle Pony Demo"

def basedict(way, msg):
    return dict(
        way=way,
        message=msg,
        year=thisyear(),
        appname=webtitle(),
        auth=True,
        name='Test',
        nick='nice',
        avatar='/static/avatar/river.jpg'
    )
