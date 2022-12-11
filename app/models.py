from sqlalchemy import Column, Integer, Boolean, Float, Date, String, Text, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship, backref
from app import app, db
from enum import Enum as UserEnum
from datetime import datetime, date


class UserRoleEnum(UserEnum):
    ADMIN = 1
    PATIENT = 2
    DOCTOR = 3
    NURSE = 4
    CASHIER = 5


class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)


class User(BaseModel):
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    avatar = Column(String(100))
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.PATIENT)
    active = Column(Boolean, default=True)
    # start_work_date = Column(Date, nullable=True)
    # checkups = relationship('Checkup', backref='user', lazy=True)
    # appointments = relationship('Appointments', backref='user', lazy=True)

    def __str__(self):
        return self.name

# class Medicine(BaseModel):
#     name = Column(String(50), nullable=False)
#     unit = Column(String(50), nullable=False)
#     price = Column(Float, nullable=False)
#     in_stock = Column(Boolean, nullable=False)
#     exp_date = Column(Date, nullable=False)


#     def __str__(self):
#         return self.name

# class MedicineCategory(BaseModel):
#     name = Column(String(50), nullable=False)
#     # medicines = relationship('Medicine', backref='category', lazy=False)


class Appointment(BaseModel):
    patient_name = Column(String(50), nullable=False)
    sex = Column(String(20), nullable=False)
    birth_date = Column(Date, nullable=False)
    # schedule = relationship('Schedule', backref='appointment', lazy=False)

    def __str__(self):
        return self.patient_name


class Schedule(BaseModel):
    appointment_date = Column(Date, nullable=False)
    appointments = Column(Integer, ForeignKey("appointment.id"), nullable=False)
    # users = relationship('User', backref='schedule', lazy=True)

# class Receipt(BaseModel):
#     checkup_date = Column(Date, nullable=False)
#     checkup_fees = Column(Float, nullable=False)
#     medicine_fees = Column(Float, nullable=False)
#     # prescription = relationship('Prescription', backref='receipt', lazy=True)

    
# class Checkup(BaseModel):
#     checkup_date = Column(Date, nullable=False)
#     symptoms = Column(String(100), nullable=False)
#     predict = Column(String(100), nullable=False)
#     checkup_user = relationship('User', backref='checkup', lazy=True)


# class Prescription(BaseModel):
#     #details = relationship('PrescriptionDetails', backref='prescription', lazy=True)
#     pass

# class PrescriptionDetails(BaseModel):
#     name = Column(String(50), nullable=False)
#     unit = Column(String(50), nullable=False)
#     usage = Column(String (100), nullable=False)


if __name__ == "__main__":
    with app.app_context():
        # a = Appointment(patient_name='Phan', sex='Male', birth_date=date(1995, 11, 3))
        # db.session.add(a)
        # db.session.commit()
        db.create_all()
        