from app.models import Appointment
from app import db, app
from sqlalchemy import func, Column, Date
from datetime import date

# def save_appointment(patient_name, sex, birth_date):
#     appointment = Appointment(patient_name, sex, birth_date)
#     db.session.add(appointment)
#     db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        db.session.add(Appointment("Phan", "Male", date(1945, 11, 3)))
        db.commit()