from flask import Flask,render_template,request
import json
import sqlite3
app=Flask(__name__)

@app.route('/$old')
def homepage():
    return render_template("welcome.html")

@app.route('/$old/signup',methods=['POST','GET'])
def signup():
    return render_template("login.html")

@app.route('/$old/signup_post',methods=['POST'])
def homepage_signup_success():
    uname_signup=request.form['uname_signup']
    pwd_signup=request.form['pwd_signup']
    email_signup=request.form['email_signup']

    conn=sqlite3.connect('/home/aravind/Desktop/SWProject/sold_database.db')
    c=conn.cursor()
    c.execute('''Select email from User where username=? ''',(str(uname_signup),))
    
    if len(c.fetchall())==0: 
        c.execute('''INSERT INTO User values (?,?,?)''',(str(uname_signup),str(email_signup),str(pwd_signup)))
        conn.commit()
        conn.close()
        successmsg="Account created successfully"
        return render_template("welcome.html",successmsg=successmsg)

    else:
        error='Username already exists,try a different name'
        conn.close()
        return render_template("login.html",error=error,username=uname_signup)


@app.route('/$old/validatelogin',methods=['POST'])
def validatelogin():
    uname=request.form['uname_login']
    pwd=request.form['pwd_login']

    conn=sqlite3.connect('/home/aravind/Desktop/SWProject/sold_database.db')
    c=conn.cursor()
    c.execute('''Select * from User where username=? ''',(str(uname),))
    data=list(c.fetchall())
    list_usernames=list(data[0][0] for i in range (len(data)))
    list_passwords=list(data[i][2] for i in range (len(data)))
    conn.close()

    if uname not in list_usernames:
        errormsg="Username does not exist, register now to login"    
        return render_template("welcome.html",error=errormsg)
    
    elif pwd!=list_passwords[list_usernames.index(uname)]:
        errormsg="Invalid Login Credentials"
        return render_template("welcome.html",error=errormsg)
    
    else:
        return render_template("SellForm.html",username=uname)

@app.route('/$old/postedproduct',methods=['POST'])
def postedproduct():
    pname=request.form['pname']
    ptype=request.form['ptype']
    initbid=request.form['initbid']
    minbid=request.form['bidincrement']
    validuntil=request.form['validuntil']
    uname=request.form['uname']

    conn=sqlite3.connect('/home/aravind/Desktop/SWProject/sold_database.db')
    c=conn.cursor()
    
    c.execute('''Select max(rowid) from Products''')
    pcount=c.fetchone()[0]

    if pcount is None:
        pcount=0
    
    if validuntil is None:
        validuntil='2019-12-12'

    pid='prod'+str(pcount+1)
    c.execute('''Insert into Products values (?,?,?,?,?,?,?,?)''',(pid,pname,ptype,initbid,minbid,validuntil,uname,uname))
    conn.commit()
    conn.close()
    return render_template("show_success_message.html",pname=pname,ptype=ptype,initbid=initbid,uname=uname,validuntil=validuntil)

@app.route('/$old/showproductlist')
def showproductlist():
    conn=sqlite3.connect('/home/aravind/Desktop/SWProject/sold_database.db')
    c=conn.cursor()
    c.execute('''Select * from Products''')
    data=list(c.fetchall())
    conn.close()
    
    return render_template("listings.html",data=data)

@app.route('/$old/mybids',methods=['POST'])
def showmybids():
    username=request.form['username']

    conn=sqlite3.connect('/home/aravind/Desktop/SWProject/sold_database.db')
    c=conn.cursor()
    c.execute('''Select * from Products''')
    details=c.fetchall()

    mybid_details=[]

    for i in range(len(details)):
        if details[i][6]==username:
            mybid_details.append(list(details[i]))

    return render_template("MyGoods.html",data=mybid_details)

@app.route('/$old/mygoods',methods=['POST'])
def showmygoods():
    username=request.form['username']

    conn=sqlite3.connect('/home/aravind/Desktop/SWProject/sold_database.db')
    c=conn.cursor()
    c.execute('''Select * from Products''')
    details=c.fetchall()
    conn.close()
    mypost_details=[]

    for i in range(len(details)):
        if details[i][6]==username:
            mypost_details.append(list(details[i]))

    return render_template("MyGoods.html",data=mypost_details)

@app.route('/$old/goback_post',methods=['POST'])
def post():
    uname=request.form['uname']
    return render_template("SellForm.html",username=uname)

if __name__=='__main__':
    app.run(port=5000)