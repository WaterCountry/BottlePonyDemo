"""
Routes and views for the bottle application.
"""
from bottle import route, view
from config import basedict,faviconico
from bill import  *

@route('/favicon.ico')
def favicon():
    return faviconico

@route('/logout')
@view('home')
def logout():
    based = basedict("Home", "首页")
    based['auth']=False
    return based

@route('/login')
@view('home')
def login():
    based = basedict("Home", "首页")
    based['auth'] = True
    return based

@route('/')
@route('/home')
@view('home')
def home():
    """Renders the home page."""
    based = basedict("Home", "首页")
    return based

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""

    based = basedict("Contact", "联系")
    return based

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    based = basedict("About", "关于")
    return based


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

@route('/list')
@view('list')
def listtitle():
    arts=listarticle()
    d1={ 'arts': arts }
    based = basedict("articlelist","文章列表")
    d1.update(based)
    return  d1
