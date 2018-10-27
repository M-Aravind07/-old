from flask import Flask,render_template,request
import sqlite3
app=Flask(__name__)

@app.route('/$old')
def homepage():
    return render_template("welcome.html")

@app.route('/$old/signup',methods=['POST','GET'])
def signup():
    return render_template("login.html")

@app.route('/$old/signup_success',methods=['GET','POST'])
def homepage_signup_success():
    successmsg="Account created successfully"
    return render_template("welcome.html",successmsg=successmsg)

@app.route('/$old/post',methods=['GET','POST'])
def post():
    return render_template("SellForm.html")

@app.route('/$old/postedproduct',methods=['GET','POST'])
def postedproduct():
    return render_template("show_success_message.html")

@app.route('/$old/showproductlist')
def showproductlist():
    return render_template("listings.html")

if __name__=='__main__':
    app.run()