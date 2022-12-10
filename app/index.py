from flask import render_template, request
from app import dao
import sys
                          
sys.path.append("./")  

from app import app

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/')
def index():
  return render_template('index.html')

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

@app.route('/create_appointment', methods=['GET', 'POST'])
def create_schedule():
  if request.method == 'POST':
    patient_name = request.form['patientName']
    sex = request.form['sex']
    birth_date = request.form['birthDate']
    # dao.save_appointment(patient_name=patient_name, sex=sex, birth_date=birth_date)
  return render_template('appointment.html')

@app.route('/dashboard')
def dashboard():
  return render_template('dashboard.html')


if __name__ == '__main__':
  app.run(debug=True)