"""
Routes and views for the bottle application.
"""

from bottle import route, view, get, post, request
from datetime import datetime
from Gux import MyDataBase

mdb = MyDataBase()

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(year=datetime.now().year)

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(title='Contact',
        message='Your contact page.',
        year=datetime.now().year)

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(title='About',
        message='Your application description page.',
        year=datetime.now().year)

@route('/login')
@view('login')
def login():
    """这是一个登陆界面."""
    return dict(title='登陆',
        message='这是一个登陆界面.',
        year=datetime.now().year)


@route('/TaskAdd', method=['POST','GET'])
@view('taskAdd')
def taskAdd():
    if(request.method == "GET"):
        return dict(title='添加任务',
            message='这是一个添加任务界面.',
            year=datetime.now().year)
    if(request.method == "POST"):
        taskName = request.forms.get('taskName')     
        taskUrl = request.forms.get('taskUrl')      
        #print('taskName= '+taskName+' taskUrl= '+taskUrl) # test
        
        mdb.executeNullReturn("INSERT INTO task VALUES (null, " + taskName + ", " + taskUrl + ", " + taskUrl + ", 1);")
        return "<p>add Success. </p>"








@route('/TaskList')
@view('taskList')
def taskList():
    """这是一个任务列表界面."""
    json = mdb.execute("select * from task")

    return dict(title='任务列表',
        message='这是一个任务列表界面.',
        data=json ,
        year=datetime.now().year)
