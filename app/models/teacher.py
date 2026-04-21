from sqlalchemy import Column, Integer, String, DateTime
from app.db.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)
    role = Column(String, default="teacher")
    teacher_id = Column(String, unique=True, index=True)
    name = Column(String)
    subject = Column(String)
    phone = Column(String)
    address = Column(String)
    gender = Column(String)
    dob = Column(String)
    blood_group = Column(String)
    religion = Column(String)
    nationality = Column(String)
    cast = Column(String)
    community = Column(String)
    status = Column(Integer, default=1) 
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    schedules = relationship("Schedule", back_populates="teacher")