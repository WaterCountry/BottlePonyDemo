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
    name='Test'
    authed=False
    s=request.environ.get('beaker.session')
    loginuser=s.get('user')

    if loginuser:
       authed=True
       name=loginuser

    return dict(
        way=way,
        message=msg,
        year=thisyear(),
        appname=webtitle(),
        auth=authed,
        name=name,
        nick='nice',
        avatar='/static/avatar/river.jpg'
    )
