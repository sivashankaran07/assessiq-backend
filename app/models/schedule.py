from sqlalchemy import Column, Integer, String, DateTime, ForeignKey,Date,Time
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime


class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(Integer ,primary_key=True ,index=True)
    teacher_id = Column(Integer,ForeignKey("teachers.id"))
    class_id = Column(Integer,ForeignKey("classes.id"),index=True)
    subject_id = Column(Integer,ForeignKey("subjects.id"),index=True)  
    date = Column(Date)
    start_time = Column(Time)
    end_time = Column(Time) 
    type = Column(Integer,index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 

    teacher = relationship("Teacher", back_populates="schedules")
    class_  = relationship("Class", back_populates="schedules")
    subject = relationship("Subject", back_populates="schedules")