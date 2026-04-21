from sqlalchemy import Column,Integer,String,DateTime
from app.db.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    schedules = relationship("Schedule", back_populates="subject")