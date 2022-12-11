from flask import render_template, request, redirect, url_for
from app import dao
from flask import render_template, request
import sys
                          
sys.path.append("./")  
from app import dao, app


@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/register', methods=['get', 'post'])
def user_register():
  err_msg=''
  if request.method.__eq__('POST'):
    name = request.form.get('name')
    username = request.form.get('username')
    password = request.form.get('password')
    confirm = request.form.get('confirmpassword')
    try:
      if password.strip().__eq__(confirm.strip()):
        dao.add_user(name=name, username=username, password=password)
        return redirect(url_for('user_register'))
      else:
        err_msg = 'Password not match'
    except Exception as ex:
      err_msg = 'Request Error ' + str(ex) 
  return render_template('register.html', err_msg=err_msg)

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
    dao.save_appointment(patient_name=patient_name, sex=sex, birth_date=birth_date)
  return render_template('appointment.html')

@app.route('/checkup')
def create_checkup():
  return render_template('create_checkup.html')

@app.route('/create_bill')
def create_bill():
  return render_template('create_bill.html')

@app.route('/dashboard')
def dashboard():
  return render_template('dashboard.html')

@app.route('/create_schedule', methods=['GET', 'POST'])
def create_sched():
  patients = dao.get_patients_list()
  return render_template('create_schedule.html', patients=patients)

@app.route('/create_schedule/save_list')
def save_list():
  patients = dao.get_patients_ids()
  dao.save_schedule(patients=patients)
  return redirect('/create_schedule')
  


if __name__ == '__main__':
  app.run(debug=True)