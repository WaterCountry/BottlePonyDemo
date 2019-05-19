"""
Routes and views for the bottle application.
"""
from bottle import route, view,request,template,redirect
from config import basedict,faviconico
from bill import  *

@route('/favicon.ico')
def favicon():
    return faviconico

@route('/logout')
@view('home')
def logout():
    s=request.environ.get('beaker.session')
    s['user']=None
    s.save()
    based = basedict("Home", "首页")
    return based

@route('/login')
@view('login')
def login():
    based = basedict("Home", "首页")
    return based

@route('/login',method='GET')
@view('login')
def login():
    username=request.query.username
    password=request.query.password
    if username.strip() and password.strip():
        if check_login(username,password):
            s=request.environ.get('beaker.session')
            s['user']=username
            s.save()
            redirect('/')
    based = basedict("Home", "首页")
    return based

@route('/')
@route('/home')
@view('home')
def home():
    """Renders the home page."""
    based = basedict("Home", "首页")
    return based

@route('/contact')
def contact():
    """Renders the contact page."""
    based = basedict("Contact", "联系")
    if based['auth']:
        return template('contact',based)
    else:
        based['message']='登录后可见!'
        return template('note',based)

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
