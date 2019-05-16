from pony.orm import Database,Required,Set
import datetime

db=Database()

class Member(db.Entity):
    role=Required(str)
    name=Required(str)
    nick=Required(str)
    password=Required(str)
    regdate=Required(datetime.date)
    active=Required(bool)
    articles=Set("Article")

class Article(db.Entity):
    title=Required(str)
    content=Required(str)
    publish=Required(bool)
    author=Required(Member)
