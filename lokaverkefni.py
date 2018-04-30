from bottle import *

@route('/')
def index():
    return template("lok.tpl")

@error(404)
def villa(error):
    return("vefsíða ekki til")

run()
