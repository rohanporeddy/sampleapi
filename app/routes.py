
from app import app
import json

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Rohan'}
    return json.dumps(user)

@app.route('/homepage')
def homepage():
    user = {'username' : 'Rohan'}
    posts = [
        {
            'author' : {'username' : 'sravan'},
            'body'   : 'When there is will there is a way'
        },
        {
            'author' : {'username' : 'nagesh'},
            'body' : 'like what you do and do what you like'
        },
        {
            'author' : {'username' : 'srikar'},
            'body' : 'hardwork is always greater than talent'
        }
    ]
    return json.dumps({
        "user" : user,
        "posts" : posts
    })
@app.route('/profilepage')
def profilepage():
    posts = [
        {
            'author' : {'username' : 'sravan'},
            'body'   : 'When there is will there is a way'
        },
        {
            'author' : {'username' : 'nagesh'},
            'body' : 'like what you do and do what you like'
        },
        {
            'author' : {'username' : 'srikar'},
            'body' : 'hardwork is always greater than talent'
        }
    ]
    return json.dumps(posts)


