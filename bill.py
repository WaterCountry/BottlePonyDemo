from pony.orm import *
from models import Member,Article,db
from datetime import datetime
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
    return select(m.nick for m in Member if m.name==username and m.password==password).first()

@db_session
def addmember():
    m1=Member(role='1',name='zhou',nick='fun',password='123',regdate=today,active=True)
    m2=Member(role='1',name='xiao',nick='live',password='123',regdate=today,active=True)
    return m1.nick+m2.nick

@db_session
def addarticle():
    member_id=1
    a1=Article(title='Every day',content='Meet a better self every day ! ',publish=True,update=today,author=member_id)
    a2=Article(title='Good luck!',content='Every one has a good luck ! ',publish=True,update=today,author=member_id)
    return a1.title+a2.title

@db_session
def showmember():
    m1=Member[1]
    return m1.to_dict()

@db_session
def showarticle():
    a1=Article[1]
    return a1.to_dict()

@db_session
def listarticle():
    arts=select(a for a in Article )
    return arts.fetch()

'''
addmember()
addarticle()
'''