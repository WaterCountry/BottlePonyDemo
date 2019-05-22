from pony.orm import *
from models import Member,Article,db
from datetime import datetime
from bottle import request
#import  os

dbfile="demo.sqlite"
today = datetime.now()


db.bind(provider='sqlite', filename=dbfile, create_db=True)
sql_debug(True)
db.generate_mapping(create_tables=True)

@db_session
def registermember(username,password,nick):
    madd=Member(role='1',name=username,nick=nick,password=password,regdate=today,active=True)
    return madd.active

@db_session
def check_login(username,password):
    mb= select(m for m in Member if m.name==username and m.password==password).first()
    return mb

@db_session
def addmember():
    m1=Member(role='1',name='zhou',nick='fun',password='123',regdate=today,active=True)
    m2=Member(role='1',name='xiao',nick='live',password='123',regdate=today,active=True)
    return m1.nick+m2.nick

@db_session
def addarticle(title,content):
    member_id=1
    ac=Article(title=title,content=content,publish=True,update=today,author=Member[member_id])

    return ac

@db_session
def showmember():
    s=request.environ.get('beaker.session')
    mid = s.get('id')
    if mid:
        m1=Member[mid]
        return m1
    else:
        return None

@db_session
def showarticle(aid):
    a1=Article[aid]
    return a1

@db_session
def listarticle():
    arts=select(a for a in Article )
    return arts


@db_session
def pagearticle(pnum,psize):
    arts=select(a for a in Article).page(pnum,pagesize=psize)
    return arts.fetch()
'''
addmember()
addarticle()
'''