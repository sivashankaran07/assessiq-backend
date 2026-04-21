from sqlalchemy import Column, Integer, String, DateTime,ForeignKey
from app.db.database import Base
from datetime import datetime


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    role = Column(String, default="student")
    roll_no = Column(String, unique=True, index=True)
    class_id = Column(Integer,ForeignKey("classes.id"))
    std = Column(String)
    father_name = Column(String)
    mother_name = Column(String)
    father_occupation = Column(String)
    mother_occupation = Column(String)
    address = Column(String)
    phone = Column(String)
    dob = Column(String)
    gender = Column(String)
    blood_group = Column(String)
    religion = Column(String)
    nationality = Column(String)
    cast = Column(String)
    community = Column(String)
    status = Column(Integer, default=1)  # 1=active, 2=inactive
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
