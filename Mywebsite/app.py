from datetime import datetime
from flask import Flask,render_template,request,redirect


app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    
    return render_template("./index.html")

@app.route("/submitform",methods=['GET','OPTIONS','POST'])
def submitform():
    if request.method=="POST":
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        print(email,subject,message)
        return "success"
    return "None"
if __name__ == '__main__':
    app.run(debug=True)

    