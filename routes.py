"""
Routes and views for the bottle application.
"""
from bottle import route, view,template,redirect
from config import basedict,faviconico
from bill import  *
from pony.orm import db_session


@route('/register')
@view('register')
def register():
    based = basedict("Home", "首页")
    return based

@route('/register',method='POST')
@view('register')
def register():
    username = request.forms.username
    password = request.forms.password
    nick = request.forms.nick

    if username.strip() and password.strip():
        if registermember(username, password,nick):
            s = request.environ.get('beaker.session')
            s['user'] = username
            s['nick'] = nick
            s.save()
            redirect('/')
        else:
            return "用户名已经存在！"
    based = basedict("Home", "首页")
    return based

@route('/logout')
@view('home')
def logout():
    s=request.environ.get('beaker.session')
    s.delete()

    based = basedict("Home", "首页")
    return based

@route('/login')
@view('login')
def login():
    based = basedict("Home", "首页")
    return based

@route('/login',method='POST')
@view('login')
def login():
    #username=request.query.username
    #password=request.query.password
    username = request.forms.username
    password = request.forms.password

    if username.strip() and password.strip():
        mb=check_login(username,password)
        if mb:
            s=request.environ.get('beaker.session')
            s['user']=mb.name
            s['nick'] =mb.nick
            s['id']=mb.id
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

    dd={'member':ms}
    dd.update(based)
    return dd


@route('/article/<aid>')
@view('article')
def article(aid):
    ac=showarticle(aid)
    based = basedict("article", "文章显示")

    dd={'article':ac}
    dd.update(based)
    return dd

@route('/article')
@db_session
def listtitle():
    page=request.query.page or '1'
    plimit=3
    arts=select(a for a in Article )
    artscount=arts.count()
    pnum= int( artscount/plimit+2)
    arts=arts.page(int(page),plimit)
    return template('list', arts=arts,pagecount=pnum, auth=False)


@route('/favicon.ico')
def favicon():
    return faviconico


@route('/add',method='POST')
@view('add')
def add():
    title = request.forms.title
    content = request.forms.content
    ac= addarticle(title,content)
    aid=ac.id
    return template('title id ={{ msg }}',msg=aid)


@route('/add')
@view('add')
def add():
    based = basedict("Home", "首页")
    return based
