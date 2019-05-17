"""
Routes and views for the bottle application.
"""

from bottle import route, view,redirect
from config import thisyear,webtitle
from bill import  *

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=thisyear(),
        appname=webtitle()
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=thisyear(),
        appname=webtitle()
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=thisyear(),
        appname=webtitle()
    )


@route('/init')
def init():
    initdb()
    addmember()
    addarticle()
    redirect('/')

@route('/member')
@view('member')
def member():
    ms= showmember()
    based=basedict("member","成员信息")
    ms.update(based)
    return ms

@route('/article')
@view('article')
def article():
    ac=showarticle()
    based = basedict("article","文章显示")
    ac.update(based)
    return ac

def basedict(t, msg):
    return dict(
        title=t,
        message=msg,
        year=thisyear(),
        appname=webtitle()
    )