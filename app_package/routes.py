from flask import render_template
from app_package import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Pawel'}
    return render_template('index.html', title='Home', user=user)
