from pony.orm import sql_debug,db_session
from models import Member,Article,db
from datetime import datetime
from common import *

today = datetime.now()

def initdb():
    db.bind('sqlite', ':memory:', create_db=True)
    sql_debug(True)
    db.generate_mapping(create_tables=True)

@db_session
def addmember():
    m=Member(role='1',name='zhou',nick='fun',password='123',regdate=today,active=True)
    return m

@db_session
def addarticle():
    member_id=1
    a=Article(title='Every day',content='Meet a better self every day ! ',publish=True,update=today,author=member_id)
    return a

@db_session
def showmember():
    member=Member[1]
    return props(member)

@db_session
def showarticle():
    article=Article[1]
    return props(article)