from flask import render_template, request, redirect, url_for, session
from app import dao, login
from app.admin import *
from flask import render_template, request
import sys, datetime
from app.models import UserRoleEnum
from flask_login import login_user, current_user, logout_user, AnonymousUserMixin
from app.utils import load_json
                          
sys.path.append("./")  
from app import dao, app


@app.route('/signin', methods=['get', 'post'])
def user_signin():
  err_msg=''
  if request.method.__eq__('POST'):
    username = request.form.get('username')
    password = request.form.get('password')

    user = dao.check_login(username=username, password=password)
    
    if user:
      if user.user_role.name == 'ADMIN':
        return redirect(url_for('admin_signin'))
      else:
        login_user(user=user)
        return redirect(url_for('dashboard'))
    else:
      err_msg = 'Username or Password is Invalid'


  return render_template('signin.html', err_msg=err_msg)

@app.route('/login-admin', methods=['get','post'])
def admin_signin():
  if request.method.__eq__('POST'):
    username = request.form.get('username')
    password = request.form.get('password')

    user = dao.check_login_admin(username=username, password=password, role=UserRoleEnum.ADMIN)
    
    if user:
      login_user(user=user)
  return redirect('/admin')

  

@login.user_loader
def user_load(user_id):
  return dao.get_user_by_id(user_id=user_id)

@app.route('/logout-user')
def user_logout():
  logout_user()
  return redirect(url_for('user_signin'))

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/register', methods=['get', 'post'])
def user_register():
  err_msg=' '
  if request.method.__eq__('POST'):
    name = request.form.get('name')
    username = request.form.get('username')
    password = request.form.get('password')
    confirm = request.form.get('confirmpassword')
    try:
      if password.strip().__eq__(confirm.strip()):
        dao.add_user(name=name, username=username, password=password)
        return redirect(url_for('user_signin'))
      else:
        err_msg = 'Password not match'
    except Exception as ex:
      err_msg = 'Request Error ' + str(ex) 
  return render_template('register.html', err_msg=err_msg)

@app.route('/home')
def home():
  return render_template('home.html')

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

@app.route('/create_appointment', methods=['GET', 'POST'])
def create_appointment():
  if request.method == 'POST':
    patient_name = request.form['patientName']
    sex = request.form['sex']
    birth_date = request.form['birthDate']
    dao.save_appointment(patient_name=patient_name, sex=sex, birth_date=birth_date)
  return render_template('appointment.html')


@app.route('/create_bill')
def create_bill():
  return render_template('create_bill.html')

@app.route('/dashboard', methods=['get', 'post'])
def dashboard():
  return render_template('dashboard.html')


@app.route('/create_schedule', methods=['GET', 'POST'])
def create_schedule():
  patients = dao.get_patients_list()
  return render_template('create_schedule.html', patients=patients)


@app.route('/create_schedule/save_list')
def save_list():
  patients = dao.get_patients_list()
  dao.save_schedule(patients=patients)

  return redirect('/create_schedule')

@app.route('/checkup')
def create_checkup():
  return render_template('create_checkup.html')
  
@app.route('/api/prescription')
def add_prescription():
  detail_id=''
  dose=''
  usage=''
  medicine_id=''
  unit=''
  prescription = session.get('prescription')
  if prescription:
    prescription = []
  
  if medicine_id in prescription:
    return
  else:
    prescription_data = {
      'id': detail_id, 
      'dose': dose,
      'usage': usage,
      'medicine_id': medicine_id,
      'unit': unit
    }
    prescription.append(prescription_data)
  
  session['prescription'] = prescription

@app.context_processor
def common_data():
  if hasattr(current_user, 'user_role'):
    image_data = load_json()
    image = ''
    for k in image_data:
      if k == current_user.user_role.name:
        image = image_data[k]
    return {
      'image' : image
    }
  else:
    return {
      'image' : ' '
    }
def inject_date():
  return {
    'today_date': datetime.date.today()
  }

if __name__ == '__main__':
  app.run(debug=True)