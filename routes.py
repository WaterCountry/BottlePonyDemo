"""
Routes and views for the bottle application.
"""

from bottle import route, view
from config import thisyear,webtitle


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

