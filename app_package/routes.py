from flask import render_template
from app_package import app
from app_package.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Pawel'}

    posts = [
        {
            'author': {'username': 'Pawel'},
            'body': 'Beautiful day in Poland'
         },
        {
            'author': {'username': 'Kasia'},
            'body': 'Chce ciuchy'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)