from sqlalchemy import Column, Integer, Boolean, Float, Date, String, Text, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship, backref
from app import app, db
from enum import Enum as UserEnum
from datetime import datetime


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
    email = Column(String(50))
    name = Column(String(50), nullable=False)
    avatar = Column(String(100))
    
    def __str__(self):
        return self.name

class Medicine(BaseModel):
    name = Column(String(50), nullable=False)
    unit = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    in_stock = Column(Boolean, nullable=False)
    exp_date = Column(Date, nullable=False)


    def __str__(self):
        return self.name

class MedicineCategory(BaseModel):
    name = Column(String(50), nullable=False)

class Staff(BaseModel):
    start_work_date = Column(Date, nullable=False)

class Appointment(BaseModel):
    patient_name = Column(String(50), nullable=False)
    sex = Column(String(20), nullable=False)
    birth_date = Column(Date, nullable=False)

class Schedule(BaseModel):
    appointment_date = Column(Date, nullable=False)

class Receipt(BaseModel):
    checkup_date = Column(Date, nullable=False)
    checkup_fees = Column(Float, nullable=False)
    medicine_fees = Column(Float, nullable=False)

class Prescription(BaseModel):
    pass

class PrescriptionDetails(BaseModel):
    name = Column(String(50), nullable=False)
    unit = Column(String(50), nullable=False)
    usage = Column(String (100), nullable=False)

