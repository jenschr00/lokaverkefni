from bottle import *
import urllib.request, json, os


@route('/')
def index():
    return template("lok.tpl")

@route('/bill')
def bill():
    n=request.forms.get('bilnumer')
    #a="http://apis.is/car?number="+str(n)
    with urllib.request.urlopen("http://apis.is/car?number={{n}}") as url:
        data = json.loads(url.read().decode())
    return template("lok2.tpl")

@error(404)
def villa(error):
    return("vefsíða ekki til")

@route('/static/<skra>')
def static_dot(skra):
    return static_file(skra, root='./')

run(host='localhost', port=8090)
