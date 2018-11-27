from bottle import *
import pymysql

database = pymysql.connect(host='tsuts.tskoli.is',user='0908012440',password='mypassword',db='0908012440_carsales',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
curs=database.cursor()

data = {'title':''}

@route('/')
def index():
    data['title']='Bílasala'
    return template("lok.tpl",data)

@route('/bill',method="POST")
def bill():
    n=request.forms.get('bilnumer')
    sqlquerry ="SELECT * FROM cars WHERE PlateNumber LIKE '%s'"%str("%"+n+"%")
    curs.execute(sqlquerry)
    result = curs.fetchall()
    print(result)
    return template("lok2.tpl")

@error(404)
def villa(error):
    return("vefsíða ekki til")

@route('/static/<skra:path>')
def static_dot(skra):
    return static_file(skra, root='./')

run(host='localhost', port=8090)
