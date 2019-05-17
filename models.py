from pony.orm import Required,Set,Database
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
    update=Required(datetime.date)
    author=Required(Member)


