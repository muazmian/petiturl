from flask import render_template
from app import app
from .url import Url


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Muaz'}
    return render_template('index.html', user=user)


@app.route('/petiturl')
def petitUrl():
    url = Url("www.google.com")
    return url.toId("ck")
