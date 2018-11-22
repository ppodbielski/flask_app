from flask import render_template
from app_package import app


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
