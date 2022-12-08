from flask import render_template
import sys
                          
sys.path.append("./")  

from app import app

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/')
def index():
  return render_template('home.html')

@app.route('/register')
def register():
  return render_template('register.html')

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/forgot_password')
def forgot_password():
  return render_template('forgot-password.html')

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404



if __name__ == '__main__':
  app.run(debug=True)