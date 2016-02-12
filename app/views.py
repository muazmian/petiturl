from flask import render_template
from flask import request
from app import app
from .url import Url
import json


@app.route('/', defaults={'petiturl': ''})
@app.route('/<petiturl>')
def index(petiturl):
    # id = redisConnection.set('a')
    # print 'blah blah blah === '+str(id)
    if not petiturl:
        return render_template('index.html')
    else:
        return getPetitUrl(petiturl)


@app.route('/petiturl', methods=['POST'])
def postPetitUrl():
    url = Url()

    link = request.form['url']

    petiturl = url.addPetitUrl(link)

    obj = {}
    obj['petiturl'] = petiturl
    return json.dumps(obj)


def getPetitUrl(petiturl):
    url = Url()
    link = url.getUrl(petiturl)
    return render_template('redirect.html', petiturl=link)
