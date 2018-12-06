from bottle import *
import urllib.request, json, os
import pymysql
import datetime

database = pymysql.connect(host='tsuts.tskoli.is',user='0908012440',password='mypassword',db='0908012440_carsales',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
curs=database.cursor()

data = {'title':''}


@route('/')
def index():
     data['title']='Bílasala'
     return template("lok.tpl",data)

@route('/selja')
def selja():
    return template("lok3.tpl")
@route('/skoda')
def skoda():
     sqlquerry ="SELECT * FROM cars"
     curs.execute(sqlquerry)
     result = curs.fetchall()
     return template("lok4.tpl", result=result)

@route('/sina',method="POST")
def sina():
    n=request.forms.get('bilnumer')
    sqlquerry ="SELECT * FROM cars WHERE PlateNumber LIKE '%s'"%str("%"+n+"%")
    curs.execute(sqlquerry)
    result = curs.fetchall()
    print(result)
    return template("sina.tpl",result=result)
@route('/kaupa', method='POST')
def kaupa():
     plate = request.forms.get('PlateNumber')
     sqlquerry = "INSERT INTO Orders(Car_Number,Car_Price,Order_Date) VALUES ('%s',(SELECT Price FROM CARS WHERE PlateNumber = '%s'),'%s')"%(plate,plate,'{0:%Y-%m-%d}'.format(datetime.datetime.now()))
     curs.execute(sqlquerry)
     database.commit()
     sqldelete = "DELETE FROM CARS WHERE PlateNumber = '%s'"%(plate)
     curs.execute(sqldelete)
     database.commit()
     
     
@route('/sqlimport' , method="POST")
def sqlimport():
     nafn=request.forms.get('nafn')
     bilnumer=request.forms.get('bilnumer')
     tegund=request.forms.get('tegund')
     undirtegund=request.forms.get('undirtegund')
     litur=request.forms.get('litur')
     skipting=request.forms.get('skipting')
     argerd=request.forms.get('argerd')
     verd=request.forms.get('verd')
     sjalfskiptur = 0
     beinskiptur = 0
     if skipting == "Sjálfskiptur":
          sjalfskiptur = 1
     else:
          beinskiptur = 1
     sql="INSERT INTO cars(Car_Name,PlateNumber,Manufacturer,Model,color,Sjalfskiptur,Beinskiptur,Man_Year,Price)" \
          "VALUES ('%s','%s','%s','%s','%s','%d','%d','%d','%d')"%(nafn,bilnumer,tegund,undirtegund,litur,int(sjalfskiptur),int(beinskiptur),int(argerd),int(verd))
     curs.execute(sql)
     database.commit()
@route('/login')
def login():
    return template('login.tpl',title='Login')

@route('/Signup')
def signup():
    return template('signup.tpl',title='Signup')


@route('/loginprocess', method='POST')
def processlogin():
     try:
          form_data_user = request.forms.get("username")
          form_data_password = request.forms.get("password")
          sqluser = ("SELECT UserName FROM users WHERE UserName = '%s'" % form_data_user)
          cursor.execute(sqluser)
          table_data_user = cursor.fetchall()
          userflag = False

          for i in table_data_user:
               for x in i:
                    if form_data_user == i[x]:
                         userflag = True
                    else:
                         print(x)
                         userflag = False

          if not userflag:
               return '<head><link rel="stylesheet" type="text/css" href="/normalize.css">' \
                    '<link rel="stylesheet" type="text/css" href="/skeleton.css"></head>' \
                    '<h3 class="u-full-width" style="text-align:center;">This Username dosen\'t exist</h3>' \
                    '<a href="/login" class="button">Login</a>'

          elif userflag:
               sqlpass = ("SELECT UserPassword FROM users WHERE UserName = '%s'" % form_data_user)
               curs.execute(sqlpass)
               table_data_pass = curs.fetchall()

               sqladmin = "SELECT USER_TYPE FROM USERS WHERE UserName = '%s'"%form_data_user
               curs.execute(sqladmin)
               usertype = curs.fetchall()
            
               passflag = False

               for i in table_data_pass:
                    for x in i:
                         if form_data_password == i[x]:
                              passflag = True
                         else:
                              passflag = False

               adminflag = False
               for i in usertype:
                    for x in i:
                         if i[x] == 'Admin':
                              adminflag == True
                         else:
                              adminflag == False

               if passflag and adminflag == True:
                    return template('admin.tpl',data=alldata,title='Admin')
               elif passflag and adminflag == False:
                    return template('user.tpl',title=form_data_user)
               else:
                    return '<head><link rel="stylesheet" type="text/css" href="/normalize.css">' \
                         '<link rel="stylesheet" type="text/css" href="/skeleton.css"></head>' \
                         '<h3 class="u-full-width" style="text-align:center;">This Password is wrong</h3> ' \
                         '<a href="/login" class="button">Login</a>'
     except:
          abort(404)


@route('/signupprocess', method='POST')
def signup():
    try:
        name=request.forms.get('name')
        username=request.forms.get('username')
        password=request.forms.get('password')
        makenewsql = "INSERT INTO users(UserName,Users_Name,UserPassword) VALUES('%s','%s','%s')"%(username,name,password)
        cursor.execute(makenewsql)
        database.commit()
        redirect('/login')
    except:
        return '<head><link rel="stylesheet" type="text/css" href="/normalize.css">' \
                '<link rel="stylesheet" type="text/css" href="/skeleton.css"></head>' \
                '<h3 class="u-full-width" style="text-align:center;">This Username already exists</h3>' \
                '<a href="/Signup" class="button">Signup</a>'
     

 

@error(404)
def villa(error):
    return("vefsíða ekki til")

@route('/static/<skra>')
def static_dot(skra):
    return static_file(skra, root='./')

run(host='localhost', port=8090)
