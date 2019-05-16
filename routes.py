"""
Routes and views for the bottle application.
"""

from bottle import route, view
from config import thisyear,webtitle
from dbhelp import  *

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
    tpl=" init db ok! <a href='/add'>addmember</a>"
    return  tpl

@route('/add')
def add():
    addmember()
    tpl = " add member ok! <a href='/news'>addnews</a>"
    return tpl

@route('/news')
def news():
    addarticle()
    tpl = " add article ok! <a href='/member'>show member </a>"
    return tpl

@route('/member')
@view('member')
def member():
    ms= showmember()
    return dict(
        title='Member',
        message='Member list.',
        year=thisyear(),
        appname=webtitle(),
        member=ms
    )

@route('/article')
@view('article')
def article():
    ac=showarticle()
    return dict(
        title='Article',
        message='Your application description page.',
        year=thisyear(),
        appname=webtitle(),
        article=ac
    )
