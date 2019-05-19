from datetime import datetime
from bottle import request
from beaker.middleware import SessionMiddleware

dbfile='demo.sqlite'
faviconico='/static/images/book.gif'

def thisyear():
    return datetime.now().year

def webtitle():
    return "Bottle Pony Demo"

def basedict(way, msg):
    authed=False
    s=request.environ.get('beaker.session')
    if s.get('user'):
       authed=True

    return dict(
        way=way,
        message=msg,
        year=thisyear(),
        appname=webtitle(),
        auth=authed,
        name='Test',
        nick='nice',
        avatar='/static/avatar/river.jpg'
    )
