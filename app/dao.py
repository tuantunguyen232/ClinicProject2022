from app.models import Appointment, Schedule, User
from app import db, app
from sqlalchemy import func, Column, Date
from datetime import date
import hashlib

def save_appointment(patient_name, sex, birth_date):
    appointment = Appointment(patient_name=patient_name, sex=sex, birth_date=birth_date)
    db.session.add(appointment)
    db.session.commit()
    return

def get_patients_list():
    patients = Appointment.query
    return patients.all()

def save_schedule(patients):
    schedule = Schedule(appointment_date=date.today(), appointments=patients)
    db.session.add(schedule)
    db.session.commit()

def get_patients_ids():
    patient_ids = Appointment.query
    return patient_ids.get('id')


def add_user(name, username, password, **kwargs):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    user = User(name=name.strip(), username=username.strip(), password=password, avatar=kwargs.get('avatar'))
    db.session.add(user)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        a = Appointment(patient_name="Phan", sex="Female", birth_date=date(1945, 11, 5))
        db.session.add(a)
        db.session.commit()

