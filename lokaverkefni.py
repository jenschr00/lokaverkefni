from bottle import *
import pymysql
import datetime
from sys import argv

database = pymysql.connect(host='tsuts.tskoli.is',user='0908012440',password='mypassword',db='0908012440_carsales',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
curs = database.cursor()

data = {'title': '','Usertype':'','User':''}


@route('/')
def index():
     data['title']='Bílasala'
     return template("lok.tpl",data=data)

@route('/selja')
def selja():
    return template("lok3.tpl")

@route('/skoda')
def skoda():
     sqlquerry ="SELECT * FROM cars"
     curs.execute(sqlquerry)
     result = curs.fetchall()
     return template("lok4.tpl", results=result,data=data)

@route('/sina',method="POST")
def sina():
    n=request.forms.get('bilnumer')
    sqlquerry ="SELECT * FROM cars WHERE PlateNumber LIKE '%s'"%str("%"+n+"%")
    curs.execute(sqlquerry)
    result = curs.fetchall()
    return template("sina.tpl",results=result,data=data)

@route('/solur')
def seldir():
    sqlquerry = "SELECT * FROM ORDERS"
    curs.execute(sqlquerry)
    result = curs.fetchall()
    return template("lok2.tpl",results=result)

@route('/kaupa', method='POST')
def kaupa():
     plate = request.forms.get('PlateNumber')
     sqlquerry = "INSERT INTO Orders VALUES ((SELECT User_id FROM USERS WHERE UserName = '%s'),'%s',(SELECT Price FROM CARS WHERE PlateNumber = '%s'),'%s')"%(data['User'],plate,plate,'{0:%Y-%m-%d}'.format(datetime.datetime.now()))
     curs.execute(sqlquerry)
     database.commit()
     sqldelete = "DELETE FROM CARS WHERE PlateNumber = '%s'"%(plate)
     curs.execute(sqldelete)
     database.commit()
     redirect('/')
     
     
@route('/sqlimport', method="POST")
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
     redirect('/')

@route('/login')
def login():
    if data['User'] == '':
        return template('login.tpl', title='Login')
    else:
        redirect('/')

@route('/Signup')
def signup():
    return template('signup.tpl',title='Signup')


@route('/loginprocess', method='POST')
def processlogin():
     #try:
        form_data_user = request.forms.get("username")
        form_data_password = request.forms.get("password")
        sqluser = "SELECT UserName FROM users WHERE UserName = '%s'"% form_data_user
        curs.execute(sqluser)
        table_data_user = curs.fetchall()
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
             sqlpass = "SELECT UserPassword FROM users WHERE UserName = '%s'" % form_data_user
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
                            adminflag = True
                       else:
                            adminflag = False

             if passflag and adminflag == True:
                  data['User'] = form_data_user
                  data['Usertype'] = "Admin"
                  redirect('/')
             elif passflag and adminflag == False:
                 data['User'] = form_data_user
                 data['Usertype'] = "Muggles"
                 redirect('/')
             else:
                  return '<head><link rel="stylesheet" type="text/css" href="/normalize.css">' \
                       '<link rel="stylesheet" type="text/css" href="/skeleton.css"></head>' \
                       '<h3 class="u-full-width" style="text-align:center;">This Password is wrong</h3> ' \
                       '<a href="/login" class="button">Login</a>'

     #except:
          #abort(404)
@route('/logout')
def logout():
    data['Usertype'] = ''
    data['User'] = ''
    redirect('/')


@route('/signupprocess', method='POST')
def signup():
    #try:
        name=request.forms.get('name')
        username=request.forms.get('username')
        password=request.forms.get('password')
        sqluser = "SELECT UserName FROM users WHERE UserName = '%s'"% username
        curs.execute(sqluser)
        table_data_user = curs.fetchall()
        userflag = False
        for i in table_data_user:
            for x in i:
                if username == i[x]:
                    userflag = True
                else:
                    userflag = False

        if userflag:
            return '<head><link rel="stylesheet" type="text/css" href="/normalize.css">' \
                   '<link rel="stylesheet" type="text/css" href="/skeleton.css"></head>' \
                   '<h3 class="u-full-width" style="text-align:center;">This Username already exist</h3>' \
                   '<a href="/Signup" class="button">Signup</a>'

        elif not userflag:
                makenewsql = "INSERT INTO users(UserName,Users_Name,UserPassword,USER_TYPE) VALUES('%s','%s','%s',%s)"%(username, name, password,'Muggles')
                curs.execute(makenewsql)
                database.commit()
                redirect('/login')
    #except:
        #return '<head><link rel="stylesheet" type="text/css" href="/normalize.css">' \
                #'<link rel="stylesheet" type="text/css" href="/skeleton.css"></head>' \
                #'<h3 class="u-full-width" style="text-align:center;">This Username already exists</h3>' \
                #'<a href="/Signup" class="button">Signup</a>'
     

 

@error(404)
def villa(error):
    return("vefsíða ekki til")

@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root="./Myndir/")

run(host='0.0.0.0', port=argv[1])
