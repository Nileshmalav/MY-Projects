from flask import Flask, render_template
import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyAeQ2d04ji4wx3MhEgcccYA_8Yb9JDXJUI",
    'authDomain': "movie-recommendation-38145.firebaseapp.com",
    'projectId': "movie-recommendation-38145",
    'storageBucket': "movie-recommendation-38145.appspot.com",
    'messagingSenderId': "519854541151",
    'appId': "1:519854541151:web:95d53ca54d18026cc38eea",
    'measurementId': "G-TY95BM5Z3R",
    'databaseURL':""
  }
firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

def signup(email,password):
  user=auth.create_user_with_email_and_password(email,password)
  
  pass
app = Flask(__name__)
@app.route("/")
def home():
  return render_template("login.html")



if __name__ == '__main__':
    app.run(debug=True)