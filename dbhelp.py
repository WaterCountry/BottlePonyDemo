from pony.orm import Database,sql_debug,db_session

from models import Member,Article

from datetime import datetime

db=Database('sqlite',':memory:',)

#db=Database('sqlite','demo.sqlite',create_db=True)


def init():
    sql_debug(True)
    db.generate_mapping(create_tables=True)

@db_session
def addmember():
    m=Member(role='1',name='zhou',nick='fun',password='123',regdate=datetime.date(),active=True)
    return m

@db_session
def addarticle():
    member_id=1
    a=Article(title='Every day',content='Meet a better self every day ! ',publish=True,author=member_id)